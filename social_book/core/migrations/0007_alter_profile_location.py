# Generated by Django 4.0.4 on 2022-05-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_profile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
