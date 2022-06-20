from email.policy import default
from django import forms
from .models import MenuItem, Menu

class CustomMMCF(forms.ModelMultipleChoiceField):
    
    def label_from_instance(self, menuitem):
        return  str(menuitem)
    
class CreateMenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ['menu_name', 'menu_active', 'menu_items_starters', 'menu_items_mains', 'menu_items_deserts', 'menu_items_drinks', 'menu_items_sides']
        labels = {
            'menu_name': 'Name',
            'menu_active': 'Active',
            'menu_items_starters': 'Starters',
            'menu_items_mains': 'Mains',
            'menu_items_deserts': 'Deserts',
            'menu_items_drinks': 'Drinks',
            'menu_items_sides': 'Sides'
        }
        
    menu_name = forms.CharField()
    menu_active = forms.CheckboxInput()
    menu_items_starters = CustomMMCF(
        queryset=MenuItem.objects.filter(menu_item_type='starter'),
        widget=forms.CheckboxSelectMultiple()
    )
    menu_items_mains = CustomMMCF(
        queryset=MenuItem.objects.filter(menu_item_type='main'),
        widget=forms.CheckboxSelectMultiple()
    )
    menu_items_deserts = CustomMMCF(
        queryset=MenuItem.objects.filter(menu_item_type='desert'),
        widget=forms.CheckboxSelectMultiple()
    )
    menu_items_drinks = CustomMMCF(
        queryset=MenuItem.objects.filter(menu_item_type='drink'),
        widget=forms.CheckboxSelectMultiple()
    )
    menu_items_sides = CustomMMCF(
        queryset=MenuItem.objects.filter(menu_item_type='side'),
        widget=forms.CheckboxSelectMultiple()
    )
    
    
   
    
   
    
    