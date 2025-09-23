from django.db import models
from django.contrib.auth.models import User
from core.models import Department

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(default=0)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"