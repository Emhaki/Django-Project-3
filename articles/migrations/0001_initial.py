from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('art_category', models.CharField(choices=[('서양화', '서양화'), ('동양화', '동양화'), ('판화', '판화'), ('일러스트', '일러스트'), ('조소', '조소'), ('설치미술', '설치미술'), ('사진', '사진')], max_length=10)),
                ('painted_year', models.IntegerField()),
                ('painted_way', models.CharField(max_length=50, null=True)),
                ('art_size', models.CharField(max_length=20, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('soldout', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='like_arts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
