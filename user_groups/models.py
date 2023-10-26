from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class CustomGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class CustomUser(AbstractUser):
    custom_group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
