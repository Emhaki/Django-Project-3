from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="question"
    )
    admin = models.BooleanField(default=False) # admin이 다 볼 수있게

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="question_comment"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)