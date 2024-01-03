import os

import stripe

from dotenv import load_dotenv
from django.conf import settings
from django.core.mail import send_mail

from config.settings import BASE_DIR
from courses.models import CourseSubscribe

dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)


class SendCourseUpdate:
    def __init__(self, course, message) -> None:
        self.mail_subject = f'Обновление курса {course.name}'
        self.message = message

        course_subscribes = CourseSubscribe.objects.filter(course=course)
        self.subscriber_mail_list = [sub.user.email for sub in course_subscribes]

    def send_email(self):
        send_mail(
            self.mail_subject,
            self.message,
            settings.EMAIL_HOST_USER,
            self.subscriber_mail_list,
            fail_silently=False
        )


stripe.api_key = os.getenv('STRIPE_API')


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
