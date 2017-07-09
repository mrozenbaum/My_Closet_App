from django.contrib import admin
from .models import Owner, Category, Item

# Register your models here.
# admin.site.register(Owner)
admin.site.register(Category)
# admin.site.register(Item)

class ItemInline(admin.StackedInline):
    model = Item
    extra = 3


class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner_name']}),
        ('Date Information', {'fields': ['pub_date']}),
        ('Owner Email', {'fields': ['email']}),
        ('Owner Closet Name', {'fields': ['closet_name']}),
        ('Owner Zip Code', {'fields': ['zip_code']}),
        ('Owner Bio', {'fields': ['bio']}),
    ]
    inlines = [ItemInline]
    list_display = ('owner_name', 'pub_date', 'email', 'closet_name', 'zip_code', 'bio')
    list_filter = ['pub_date']
    search_fields = ['owner_name']
    


admin.site.register(Owner, OwnerAdmin)

