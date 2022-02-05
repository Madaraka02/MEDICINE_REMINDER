from django.db import models
from django.contrib .auth.models import User

# Create your models here.
class Prescription(models.Model):
    medicine_name = models.CharField(max_length=100)
    dosage = models.TextField()
    time = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)