from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets

# Получить список всех пользователей
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Получить конкретного пользователя по ID
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API для CRUD операций над пользователями.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
