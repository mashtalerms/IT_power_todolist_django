from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegistrationView(CreateAPIView):
    """Create new user"""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# class UserListView(ListAPIView):
#     """Get list of users for me"""
#     queryset = User.objects.all()
#     serializer_class = UserListSerializer


class UserLoginView(CreateAPIView):
    """Login user"""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        # validate request data
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # authenticate
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        # login
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Invalid password']}, status=status.HTTP_400_BAD_REQUEST)
