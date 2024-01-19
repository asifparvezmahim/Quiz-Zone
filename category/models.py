from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
