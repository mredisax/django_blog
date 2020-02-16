# Generated by Django 3.0.2 on 2020-01-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/img/avatar', verbose_name='Avatar'),
        ),
    ]
