from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
