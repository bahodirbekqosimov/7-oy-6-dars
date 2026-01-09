from django.db import models
from django.contrib.auth.models import AbstractUser

class Note(models.Model):
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE, related_name="note")
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    

