import stripe
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task
from courses.models import CourseSubscribe


class SendCourseUpdate:
    def __init__(self, course, message) -> None:
        self.mail_subject = f'Обновление курса {course.name}'
        self.message = message

        course_subscribes = CourseSubscribe.objects.filter(course=course)
        self.subscriber_mail_list = [sub.user.email for sub in course_subscribes]

    @shared_task
    def send_email(self):
        send_mail(
            self.mail_subject,
            self.message,
            settings.EMAIL_HOST_USER,
            self.subscriber_mail_list,
            fail_silently=False
        )


class PaymentService:
    @staticmethod
    def create_payment_intent(amount, currency='usd'):
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                payment_method_types=['card'],
            )
            return payment_intent.client_secret
        except stripe.error.CardError as e:
            raise Exception(str(e))

    @staticmethod
    def retrieve_payment_intent(payment_intent_id):
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return payment_intent.status
        except stripe.error.InvalidRequestError as e:
            raise Exception(str(e))
