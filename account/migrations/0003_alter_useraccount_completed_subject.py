# Generated by Django 4.1 on 2022-09-13 07:06

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_quizinstance_quiz_remove_quizinstance_taker_and_more'),
        ('account', '0002_alter_useraccount_completed_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='completed_subject',
            field=models.ManyToManyField(default=django.db.models.manager.BaseManager.all, to='quiz.subject'),
        ),
    ]
