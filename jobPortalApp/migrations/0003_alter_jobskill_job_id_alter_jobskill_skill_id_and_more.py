# Generated by Django 4.0.1 on 2022-02-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0002_jobskill_seekerskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobskill',
            name='job_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jobskill',
            name='skill_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seekerskill',
            name='skill_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='seekerskill',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
