from django.db import models
from django.conf import settings
from django.contrib import admin
# Create your models here.


class Coordinator(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    @admin.display(ordering='user__full_name')
    def full_name(self):
        return self.user.full_name
    
    def __str__(self):
        return str(self.user.email)
