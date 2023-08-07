from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']
        
    
    def __str__(self):
        return self.name

class brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    category = TreeForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name