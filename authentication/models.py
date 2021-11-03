from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Creator'),
        (SUBSCRIBER, 'Subscriber'),
    )

    profile_photo = models.ImageField(
        default="default-user.jpg")
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES)

    def __str__(self) -> str:
        return self.username
