# Generated by Django 2.2.5 on 2019-10-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogpost_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
    ]
