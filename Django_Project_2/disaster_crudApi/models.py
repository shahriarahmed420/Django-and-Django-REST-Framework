from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Home & Kitchen', 'Home & Kitchen'),
        ('Books', 'Books'),
        ('Sports', 'Sports'),
    ]
    
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
