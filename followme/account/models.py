from django.db import models
from django.contrib.auth.models import (AbstractUser,
                                        BaseUserManager)

from randomizer.models import Place


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

    # def add_to_favorites(self, place):
    #     return self.favorites.add(place)
    #
    # def delete_from_favorites(self, place):
    #     return self.favorites.remove(place)


class User(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=100, blank=True, unique=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    favorites = models.ManyToManyField(Place)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username
