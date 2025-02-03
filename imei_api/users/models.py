from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Ввидите другое имя пользователя'
            )
        ],
        error_messages={
            'unique': 'Данный ник уже используется'
        },
    )
    email = models.EmailField(
        'Почта',
        max_length=254,
        unique=True,
        error_messages={
            'unique': 'Данный email уже используется'
        },
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
    )
    last_name = models.CharField('Фамилия', max_length=150,)
    tg_id = models.PositiveIntegerField('id телеграм аккаунта', blank=True)
    whtite_list = models.BooleanField(default=False)

    class Meta:
        default_related_name = 'users'
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
