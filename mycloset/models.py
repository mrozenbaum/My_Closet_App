import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Owner(models.Model):
    ''' creates Owner table in our database '''
    email = models.EmailField(max_length=254)
    owner_name = models.CharField(max_length=200)
    closet_name = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date_added')
    bio = models.CharField(max_length=200)
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'owners'
        ordering = ["-closet_name"]


    def __str__(self):
        ''' returns a string of owner text to interact with interface '''
        return self.closet_name


    # def owner_added_recently(self):
        '''
        returns boolean if an Owner (profile) was added by a user within a
        designated timeframe
        '''
        # now = timezone.now()
        # return now - datetime.timedelta(days=1) <= self.date_added <= now
        # was_added_recently.admin_order_field = 'date_added'
        # was_added_recently.boolean = True
        # was_added_recently.short_description = 'Added recently?'    



class Category(models.Model):
    ''' creates Category table in our database '''

    TOPS = 1
    BOTTOMS = 2
    OUTERWEAR = 3
    SHOES = 4
    BAGS = 5
    ACCESSORIES = 6
    JEWELRY = 7

    CATEGORY_TYPE_CHOICES = (
        (TOPS, 'Tops'),
        (BOTTOMS, 'Bottoms'),
        (OUTERWEAR, 'Outerwear'),
        (SHOES, 'Shoes'),
        (BAGS, 'Bags'),
        (ACCESSORIES, 'Accessories'),
        (JEWELRY, 'Jewelry'),
    )

    category = models.CharField(
        max_length=25,
        choices=CATEGORY_TYPE_CHOICES,
        default=TOPS, unique=True,
    )

    category_likes = models.IntegerField(default=0)

    
    class Meta:
        verbose_name_plural = 'categorys'



    def __str__(self):
        ''' returns a string of category_type text to interact with '''
        return self.category






class Item(models.Model):
    ''' creates Item table in our database '''
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=25)
    item_brand = models.CharField(max_length=25)
    item_color = models.CharField(max_length=25)
    item_price = models.IntegerField(blank=True, null=True)
    purchase_place = models.CharField(max_length=250)
    date_purchased = models.DateTimeField(blank=True, null=True)
    pub_date = models.DateTimeField('date_added')
    item_likes = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'items'

    def __str__(self):
        ''' returns a string of category_type text to interact with '''
        return self.item_name

    def item_added_recently(self):
        '''
        returns boolean if an Owner (profile) was added by a user within a
        designated timeframe
        '''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now
        was_added_recently.admin_order_field = 'date_added'
        was_added_recently.boolean = True
        was_added_recently.short_description = 'Added recently?'    

    






