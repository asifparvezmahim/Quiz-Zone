from django.contrib import admin
from .models import Category


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]


admin.site.register(Category, categoryAdmin)
