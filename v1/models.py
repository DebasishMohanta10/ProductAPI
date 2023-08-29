from django.db import models
from django_extensions.db.models import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = AutoSlugField(max_length=100,unique=True,populate_from=["name"])
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=100,unique=True,populate_from=["name"])
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name



    
