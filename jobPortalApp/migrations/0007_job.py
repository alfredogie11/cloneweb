# Generated by Django 4.0.1 on 2022-02-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobPortalApp', '0006_remove_resume_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('salary', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('company_id', models.IntegerField()),
            ],
        ),
    ]
