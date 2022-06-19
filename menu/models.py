from django.db import models
from django.contrib.auth.models import User

ITEM_TYPES = (("starter","Starter"),("main","Main"),("desert","Desert"),("drink","Drink"),("side", "Side"))


class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=50)
    menu_item_type = models.CharField(max_length=25, choices=ITEM_TYPES, default='starter')
    menu_item_description = models.TextField(default="")
    menu_item_price = models.FloatField(default=0.00)
    contains_nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-menu_item_type', 'menu_item_name']

    def __str__(self):
        return str(self.menu_item_type) + ':' + str(self.menu_item_name)
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=25)
    menu_items = models.ManyToManyField('MenuItem', related_name='menus')
    menu_active = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['menu_name']

    def __str__(self):
        return str(self.menu_name)