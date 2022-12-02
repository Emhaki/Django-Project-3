from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.ImageField(upload_to="images/", blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="questions"
  )