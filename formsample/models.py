from django.db import models

# Create your models here.

class ModelA(models.Model):
    field1 = models.CharField(max_length=10)
    field2 = models.CharField(max_length=10)
    
class ModelB(models.Model):
    field1 = models.CharField(max_length=10)
    field2 = models.CharField(max_length=10)