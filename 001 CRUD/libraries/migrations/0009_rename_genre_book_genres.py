# Generated by Django 4.0.4 on 2022-04-25 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0008_remove_book_genres_remove_book_publisher_book_genre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genres',
        ),
    ]
