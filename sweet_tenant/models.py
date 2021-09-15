from django.db import models

# Create your models here.
class Sweet(models.Model):
    name = models.CharField(max_length=128)
