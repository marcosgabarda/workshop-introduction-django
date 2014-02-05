from django.db import models

# Create your models here.


class Coffee(models.Model):
    """
    Model for coffe.
    """
    name = models.CharField(max_length=128)
    picture = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_add_now=True)