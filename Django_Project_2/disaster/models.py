from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donation(models.Model):
    donor_name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.donor_name} - {self.amount}'
    
    
class Crisis(models.Model):
    status = [
        ('open', 'open'),
        ('closed', 'closed'),
        ('pending', 'pending')
    ]
    severity = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    ]
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    status = models.CharField(max_length=10, choices=status, default='pending')
    severity = models.CharField(max_length=10, choices=severity)
    date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    required_help = models.CharField(max_length=100, default='not required')
    
    def __str__(self):
        return self.title 