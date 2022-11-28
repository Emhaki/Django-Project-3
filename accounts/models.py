from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    # 선택 항목 필드
    fullname = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    stagename = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=254,
        verbose_name="이메일 주소",
    )
    is_studentID_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    profile_picture = ProcessedImageField(
        upload_to="profile_pictures/",
        null=True,
        blank=True,
        processors=[ResizeToFill(512, 512)],
        format="JPEG",
        options={
            "quality": 60,
        },
    )
    career = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    detail_address = models.CharField(max_length=50)
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )


    def __str__(self):
        return self.username
