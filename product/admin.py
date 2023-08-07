from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

from .models import category, brand, product

admin.site.register(category, DraggableMPTTAdmin)
admin.site.register(brand)
admin.site.register(product)
