from django.contrib import admin
from .models import Owner, Category, Item

# Register your models here.
admin.site.register(Owner)
admin.site.register(Category)
admin.site.register(Item)
