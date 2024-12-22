from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer

# List View
class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
