from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(max_length=100, verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateField(verbose_name='Дата создания')
    date_edit = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'