# Generated by Django 4.1 on 2022-09-24 10:21

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_remove_subject_teacher'),
        ('account', '0005_alter_useraccount_completed_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='completed_subject',
            field=models.ManyToManyField(default=django.db.models.manager.BaseManager.all, to='quiz.subject'),
        ),
    ]
