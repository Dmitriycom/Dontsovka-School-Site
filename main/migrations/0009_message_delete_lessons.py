# Generated by Django 4.2.6 on 2023-10-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_weeklyschedule_lessons'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('description', models.TextField(max_length=250, verbose_name='Сообщение')),
                ('date', models.DateField(default='2023-01-01', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.DeleteModel(
            name='Lessons',
        ),
    ]