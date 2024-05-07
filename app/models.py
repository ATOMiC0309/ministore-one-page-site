from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='categories/', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cat_products")
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.name