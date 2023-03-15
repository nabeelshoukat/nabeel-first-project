# Generated by Django 4.1.7 on 2023-03-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_management', '0002_remove_service_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('job_title', models.CharField(blank=True, max_length=500, null=True)),
                ('twitter', models.CharField(blank=True, max_length=2000, null=True)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram', models.CharField(blank=True, max_length=2000, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]