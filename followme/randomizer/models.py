from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Tag(models.Model):
    text = models.CharField(max_length=30)
    value = models.CharField(max_length=30, default=text)

    def __str__(self):
        return f'{self.value}'


class Place(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=120)
    photo = models.URLField(max_length=300)
    address = models.CharField(max_length=300, blank=True)
    station = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name}'


class UserPlace(models.Model):
    user = models.ForeignKey('randomizer.User', on_delete=models.CASCADE)
    place = models.ForeignKey('randomizer.Place', on_delete=models.CASCADE)
    rating = models.FloatField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ])

    def __str__(self):
        return f'{self.user.username} -> {self.place.name} = {self.rating}'


class UserManager(BaseUserManager):
    def _create_user(self, first_name, last_name, username, password, **extra_fields):
        if not first_name:
            raise ValueError("Вы не ввели имя")
        if not last_name:
            raise ValueError("Вы не ввели фамилию")
        if not username:
            raise ValueError("Вы не ввели имя пользователя")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, username, password):
        return self._create_user(first_name, last_name, username, password, is_staff=False, is_superuser=False)

    def create_superuser(self, username, password, first_name='admin', last_name='admin'):
        return self._create_user(first_name, last_name, username, password, is_staff=True, is_superuser=True)


class User(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=100, blank=True, unique=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username



