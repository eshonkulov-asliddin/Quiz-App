# Generated by Django 4.1 on 2022-09-24 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_remove_quizinstance_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
    ]
