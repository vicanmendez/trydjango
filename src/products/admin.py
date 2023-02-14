from django.contrib import admin

#The model product is defined into the models.py file, which is in the same directory
#This is called a relative import (from the same directory)
from .models import Product
# Register your models here.
admin.site.register(Product)

