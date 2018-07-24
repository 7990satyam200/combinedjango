from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    new_title=models.CharField(max_length=200)
    new_body=models.TextField(max_length=200)
    
    def __str__(self):
        return self.new_title
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
