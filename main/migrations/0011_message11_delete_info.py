# Generated by Django 4.2.6 on 2023-11-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
            ],
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]