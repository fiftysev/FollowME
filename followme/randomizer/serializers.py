from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Place, Tag, User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['value', 'text']


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    # other_photos = serializers.ListSerializer(many=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'photo',
                  'address', 'description', 'station',
                  'rating', 'tags']


class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'})
    # password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password', 'confirm_password']
        # extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['is_active', 'is_staff']

    def create(self, *args, **kwargs):
        user = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают")
        user.set_password(make_password(self.validated_data['password']))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # favorites = FavoritesSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        # need to add favorites field
