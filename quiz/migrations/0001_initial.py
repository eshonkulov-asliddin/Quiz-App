# Generated by Django 4.1 on 2022-09-10 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('teacher', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('featured_image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QuizInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_taken', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('complete', models.BooleanField(blank=True, default=False, null=True)),
                ('quiz', models.ManyToManyField(to='quiz.subject')),
                ('taker', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('a', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('b', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('c', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('d', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('options', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=50, null=True)),
                ('answer', models.CharField(blank=True, max_length=50, null=True)),
                ('submitted', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.subject')),
            ],
            options={
                'ordering': ['question'],
            },
        ),
    ]
