from django.urls import path
from rest_framework import routers

from courses.apps import OnlineSchoolConfig
from courses.views import (CourseSubscribeCreateAPIView, CourseSubscribeDestroyAPIView, CourseSubscribeListAPIView,
                           CourseViewSet,
                           LessonListAPIView,
                           LessonCreateAPIView,
                           LessonRetrieveAPIView,
                           LessonUpdateAPIView,
                           LessonDestroyAPIView,
                           PaymentViewSet,
                           PaymentView)

app_name = OnlineSchoolConfig.name

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('course/subscribe/', CourseSubscribeCreateAPIView.as_view(), name='subscribe_course'),
                  path('course/unsubscribe/', CourseSubscribeDestroyAPIView.as_view(), name='unsubscribe_course'),
                  path('course/subscribe_list/', CourseSubscribeListAPIView.as_view(), name='subscribe_list'),

                  path('api/payments/create/', PaymentView.as_view(), name='create-payment'),

              ] + router.urls
