from django.views import generic
from .models import Menu, MenuItem


class MenuList(generic.ListView):
    
    model = Menu
    template_name = 'menu/menus.html'
    def get_queryset(self):
        return Menu.objects.all()
    
