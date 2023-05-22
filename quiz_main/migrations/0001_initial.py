# Generated by Django 4.2.1 on 2023-05-22 14:54

import datetime
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('max_attempts', models.PositiveIntegerField(default=1)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(default=datetime.datetime(2023, 6, 1, 14, 54, 54, 392543, tzinfo=datetime.timezone.utc))),
                ('percentage', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz_main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('T', models.CharField(help_text='НАПРИМЕР: A', max_length=200)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_main.test')),
            ],
        ),
    ]
