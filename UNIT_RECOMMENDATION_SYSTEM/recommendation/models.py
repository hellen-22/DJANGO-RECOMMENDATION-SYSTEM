from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_code = models.CharField(max_length=20)
    unit_name = models.CharField(max_length=50)

    def ___str__(self):
        return self.unit_name