from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Enrollment
from courses.models import Course
from django.utils import timezone
from .serializers import EnrollmentSerializer
from rest_framework import generics

# Function-Based View (создание записи)
def enroll_course(request, user_id, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        enrollment, created = Enrollment.objects.get_or_create(
            user_id=user_id, course_id=course.id, defaults={'enrollment_date': timezone.now(), 'status': 'active'}
        )
        status = 'created' if created else 'already enrolled'
        return JsonResponse({'enrollment_status': status})

# Class-Based View (список записей пользователя)
class UserEnrollmentsView(View):
    def get(self, request, user_id):
        enrollments = Enrollment.objects.filter(user_id=user_id).values()
        return JsonResponse({'enrollments': list(enrollments)})

class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
