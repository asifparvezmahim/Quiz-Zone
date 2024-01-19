from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class app_admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
