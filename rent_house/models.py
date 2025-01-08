from django.db import models
from django.urls import reverse

# Create your models here.


class Appartments(models.Model):
    title = models.CharField(max_length=255,verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name='Слаг')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d",default=None,blank=True,null=True,verbose_name='Фото')
    payment = models.IntegerField(verbose_name='Ежемесячная оплата')
    number_of_rooms = models.IntegerField(verbose_name='Количество комнат')
    size_of_apartment = models.FloatField(verbose_name='Квадратуры квартиры')
    floor = models.IntegerField(verbose_name='Этаж')
    furniture = models.CharField(max_length=255,blank=True,verbose_name='Мебель')
    technique = models.CharField(max_length=255,blank=True,verbose_name='Техника')
    cat = models.ForeignKey(to='Category',on_delete=models.PROTECT,related_name='posts',verbose_name='Категории')
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name= 'Квартиры'
        verbose_name_plural= 'Квартиры'


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Категории'
        verbose_name_plural= 'Категории'
