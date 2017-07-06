from django import forms

from .models import Owner, Item

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['owner_name', 'email', 'closet_name', 'zip_code', 'pub_date', 'bio']
        labels = {
        'owner_name': 'First Name',
        'email': 'Email',
        'closet_name': 'Closet Name',
        'pub_date': 'Date Added',
        'zip_code': 'Zipcode',
        'bio': 'Bio'
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_brand', 'item_color', 'item_price', 'purchase_place', 'date_purchased', 'pub_date', 'categorys']
        labels = {
        'item_name': 'Item Name',
        'item_brand': 'Item Brand',
        'item_price': 'Item Price',
        'purchase_place': 'Purchase Place',
        'pub_date': 'Date Added',
        'categorys': 'Category'
        }        