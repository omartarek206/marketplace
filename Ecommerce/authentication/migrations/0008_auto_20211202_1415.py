# Generated by Django 3.2.9 on 2021-12-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_user_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]
