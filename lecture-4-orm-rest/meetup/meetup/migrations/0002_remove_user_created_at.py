# Generated by Django 4.2.10 on 2024-02-13 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
    ]