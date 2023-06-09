# Generated by Django 4.1 on 2022-09-13 07:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_remove_quizinstance_quiz_remove_quizinstance_taker_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizinstance',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizinstance',
            name='taker',
        ),
        migrations.AddField(
            model_name='quizinstance',
            name='quiz',
            field=models.ManyToManyField(to='quiz.subject'),
        ),
        migrations.AddField(
            model_name='quizinstance',
            name='taker',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
