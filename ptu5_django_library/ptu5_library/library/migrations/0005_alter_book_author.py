# Generated by Django 4.1.3 on 2022-11-08 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_author_options_alter_genre_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.author'),
        ),
    ]
