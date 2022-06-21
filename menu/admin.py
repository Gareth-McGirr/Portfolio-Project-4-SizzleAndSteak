from django.contrib import admin
from .models import MenuItem, Menu

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'price'
    )
    list_filter = ('type',)
    
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        
        'name',
        'active',
        'created_by',
        'created_on',
        'updated_on',
    )
    list_filter = ('name',)
    
    def get_items(self, obj):
        return "\n, ".join([m.menu_item_name for m in obj.menu_items.all()])
