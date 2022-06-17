from django.views import generic

from menu.forms import CreateMenuForm
from .models import Menu, MenuItem


class MenuListView(generic.ListView):
    
    model = Menu
    template_name = 'menu/menus.html'
    def get_queryset(self):
        return Menu.objects.filter(menu_active=True)
    
class CreateMenuView(generic.CreateView):
    model = Menu
    form_class = CreateMenuForm
    template_name = 'menu/create_menu.html'
    success_url = '/menu/menus'