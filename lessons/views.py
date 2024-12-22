from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer

# List View
class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
