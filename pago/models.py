from django.db import models

# Create your models here.

class cohorte1 (models.Model):
    Nombre = models.CharField(max_length = 50)
    CI = models.CharField(max_length = 50, unique = True)
    Email = models.EmailField()
    Pagado = models.BooleanField()

