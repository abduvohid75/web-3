from django.db import models
from django.utils import timezone

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=10000, verbose_name='содержимое')
    preview = models.ImageField(verbose_name='изображение', null=True)
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='статус публикации')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'
    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'