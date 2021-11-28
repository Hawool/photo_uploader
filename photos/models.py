from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Photo(models.Model):
    """model for photos"""
    owner = models.ForeignKey(UserModel, verbose_name='Owner', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Photo')

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self):
        return self.id
