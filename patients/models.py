from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, blank=True)
    emergency_contact = models.CharField(max_length=15, blank=True)
    medical_history = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.get_full_name()
    
    def age(self):
        from datetime import date
        return (date.today() - self.date_of_birth).days // 365