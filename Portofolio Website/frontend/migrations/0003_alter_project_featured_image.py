# Generated by Django 4.0.4 on 2022-04-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='projects/default.jpg', null=True, upload_to='projects/'),
        ),
    ]
