# Generated by Django 3.0 on 2020-02-25 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20200225_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='messages',
        ),
    ]
