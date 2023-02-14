from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length is required
    description = models.TextField(blank=True, null=True) #blank=true means that the field is not required
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=True) #null=True, default=True

    def get_absolute_url(self):
        #return f"/products/{self.id}/"
        print("Llamando a la funcion get_absolute_url")
        return reverse("products:product-lookup", kwargs={"id": self.id})

