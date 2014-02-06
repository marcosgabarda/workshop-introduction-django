from django.contrib.auth.models import PermissionsMixin, AbstractUser
# Create your models here.


class User(AbstractUser, PermissionsMixin):
    """
    Coffee user.
    """


