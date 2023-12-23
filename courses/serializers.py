from rest_framework import serializers
from courses.models import Course, Lesson, Payment
from courses.permissions import CourseModeratorClass, IsModeratorClass
from rest_framework.permissions import IsAuthenticated


class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.all.count')
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'