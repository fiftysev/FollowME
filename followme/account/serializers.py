from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password', 'confirm_password']

    def save_user(self, *args, **kwargs):
        user = User(
            firstname=self.validated_data['first_name'],
            lastname=self.validated_data['last_name'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают")
        user.set_password(password)
        user.save()
        return user
