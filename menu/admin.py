from django.contrib import admin
from .models import MenuItem, Menu

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'menu_item_name',
        'menu_item_type',
        'menu_item_price'
    )
    list_filter = ('menu_item_type',)
    
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'menu_name',
        'menu_active'
    )
    list_filter = ('menu_name',)
    
    def get_items(self, obj):
        return "\n, ".join([m.menu_item_name for m in obj.menu_items.all()])
