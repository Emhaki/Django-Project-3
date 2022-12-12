from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profileimage = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
        options={"quality": 100},
    )
    nickname = models.CharField(max_length=10, blank=True)  # 본명
    creater_name = models.CharField(max_length=10, blank=True)  # 사용자의 아이디
    introduce = models.CharField(max_length=200, blank=True)  # 소개글
    refresh_token = models.TextField(blank=True)
    is_creater = models.BooleanField(default=False)
    location = models.CharField(max_length=40, blank=True)
    location_detail = models.CharField(max_length=40, blank=True)
    test = models.CharField(max_length=40, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    recently_view = models.TextField(default="")  # 최근 본 작품 목록
