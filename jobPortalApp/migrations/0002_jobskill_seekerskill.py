# Generated by Django 4.0.1 on 2022-02-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOBSKILL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.IntegerField(unique=True)),
                ('job_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SEEKERSKILL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_id', models.IntegerField(unique=True)),
                ('user_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
