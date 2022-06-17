from django.db import models
from django.contrib.auth.models import User

ITEM_TYPES = (("starter","Starter"),("main","Main"),("desert","Desert"),("drink","Drink"),("side", "Side"))


class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=25)
    menu_item_type = models.CharField(max_length=25, choices=ITEM_TYPES, default='starter')
    menu_item_price = models.FloatField()
    contains_nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['menu_item_name']

    def __str__(self):
        return str(self.menu_item_name)
    
class Menu(models.Model):
    menu_name = models.CharField(max_length=25)
    menu_items = models.ManyToManyField('MenuItem', related_name='menus')
    
    
    class Meta:
        ordering = ['menu_name']

    def __str__(self):
        return str(self.menu_name)
    


