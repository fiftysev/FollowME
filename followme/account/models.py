from django.db import models
from rest_framework import permissions
from django.contrib.auth.models import (AbstractUser,
                                        BaseUserManager)


class UserManager(BaseUserManager):
    def _create_user(self, first_name, last_name, username, password, email, **extra_fields):
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
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, username, password, email=None):
        return self._create_user(first_name, last_name, username, password, email)

    def create_superuser(self, username, password, email, first_name='admin', last_name='admin'):
        return self._create_user(first_name, last_name, username, password, email, is_staff=True, is_superuser=True)


class User(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username
