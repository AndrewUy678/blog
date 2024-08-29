from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.CharField(max_length=100, verbose_name='Контент')
    time_create = models.DateTimeField(verbose_name='Дата')
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'посты'
        verbose_name_plural = 'посты'

class NewWork(models.Model):
    file = models.ImageField(upload_to='uploads_models', default=None, blank=True, null=True, verbose_name='изображение')
    title = models.CharField(max_length=100, default=None, blank=True, null=True)
    text_content = models.CharField(max_length=100, default=None, blank=True, null=True)
    time_create_work = models.DateTimeField(verbose_name='Дата', default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'работы'
        verbose_name_plural = 'работы'