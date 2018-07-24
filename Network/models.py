from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# from django import forms
from django.conf import settings

# Create your models here.
# class twit(models.Model):
#     tweet = models.CharField(max_length=30)
#     date = models.DateTimeField(auto_now_add=True)
#     profile = models.FileField(default='SOME STRING')
#     def get_absolute_url(self):
#         return reverse('twit_detail', args=[str(self.id)])
#     def __str__(self):
#         return self.tweet



class post(models.Model):
    tweet = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.FileField(default='SOME STRING')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def get_absolute_url(self):
        return reverse('twit_detail', args=[str(self.id)])
    def __str__(self):
        return self.tweet
