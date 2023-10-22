# Generated by Django 4.2.6 on 2023-10-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default='2023-01-01', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='news',
            name='path',
            field=models.FilePathField(verbose_name='Путь'),
        ),
    ]