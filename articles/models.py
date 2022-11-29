from django.db import models
from config.settings import AUTH_USER_MODEL
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

category_choices = (
    ("서양화", "서양화"),
    ("동양화", "동양화"),
    ("판화", "판화"),
    ("일러스트", "일러스트"),
    ("조소", "조소"),
    ("설치미술", "설치미술"),
    ("사진", "사진"),
)

# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    art_category = models.CharField(max_length=10, choices=category_choices)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 800)],
                                format='JPEG',
                                options={'quality': 100},
                                null=True)
    artist = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name="작가",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    likes = models.ManyToManyField(AUTH_USER_MODEL, related_name='like_arts')

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)