from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    logo = models.URLField()

    class Meta:
        ordering = ["-id"]
        db_table = "services"
        
    def __str__(self):
         return self.name
