from sweet_shared.models import SweetType
from django.db import models

# Create your models here.
class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
