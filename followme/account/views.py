from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer


class RegistrationUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
