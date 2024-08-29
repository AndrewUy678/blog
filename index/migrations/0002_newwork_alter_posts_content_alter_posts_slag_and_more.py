# Generated by Django 5.0.7 on 2024-08-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_models', verbose_name='изображение')),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.CharField(max_length=100, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slag',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time_create',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
    ]
