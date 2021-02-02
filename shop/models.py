from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Product(models.Model):
    currency_list = (
        (None, '------------------------------'),
        ('грн.', 'UAH'),
        ('долл.', 'USD'),
        ('ев.', 'EUR'),
    )
    p_countries = (
        (None, '------------------------------'),
        ('UA', 'Украина'),
        ('RU', 'Россия'),
        ('PL', 'Польша'),
        ('BL', 'Белорусь'),
        ('CN', 'Китай'),
        ('USA', 'Америка')
    )

    title = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    producer_country = models.CharField(null=True, max_length=24, choices=p_countries, verbose_name='Країна Виробник')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    currency = models.CharField(null=True, max_length=8, choices=currency_list, verbose_name='Валюта')
    available = models.BooleanField(default=True)
    in_stock = models.PositiveIntegerField()
    category = models.ForeignKey(to='Category', null=True, on_delete=models.PROTECT, verbose_name='Категорія')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=3)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    reting = models.IntegerField(default=3)

