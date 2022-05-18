# Generated by Django 4.0.4 on 2022-05-18 21:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='feed_images')),
                ('caption', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('total_likes', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.IntegerField(editable=False),
        ),
    ]
