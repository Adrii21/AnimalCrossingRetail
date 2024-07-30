from djongo import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=155)
    theme = models.CharField(max_length=155)
    category = models.CharField(max_length=155)
    available = models.BooleanField(default=False)

    class Meta:
        db_table = 'items'
