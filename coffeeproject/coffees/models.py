from django.conf import settings
from django.db import models

# Create your models here.


class Coffee(models.Model):
    """
    A coffee type.
    """
    name = models.CharField(max_length=128)
    picture = models.ImageField(upload_to="pictures", null=True, blank=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="coffees_created")
    created_at = models.DateTimeField(auto_now_add=True)


class CoffeeTaken(models.Model):
    """
    User drinks coffee.
    """
    coffee = models.ForeignKey(Coffee, related_name="users_taken")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="coffees_taken")

    created_at = models.DateTimeField(auto_now_add=True)