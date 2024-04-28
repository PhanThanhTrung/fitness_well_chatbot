# Generated by Django 4.1.2 on 2024-04-28 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('exercise_type', models.CharField(blank=True, max_length=200)),
                ('main_muscle', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 4, 28, 9, 3, 53, 755638, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tools_required', models.CharField(blank=True, max_length=200)),
                ('tier', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]