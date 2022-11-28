from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

# Create your models here.
class Art(models.Model):
    artist = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="작가",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    art_category = models.CharField(max_length=50)
    introduce = models.CharField(max_length=200)
    price = models.PositiveIntegerField(blank=True, null=True)
