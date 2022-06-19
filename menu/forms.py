from email.policy import default
from django import forms
from .models import MenuItem, Menu

class CustomMMCF(forms.ModelMultipleChoiceField):
    
    def label_from_instance(self, menuitem):
        return  str(menuitem)
    
class CreateMenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ['menu_name', 'menu_active', 'menu_items']
        labels = {
            'menu_name': 'Name',
            'menu_active': 'Active',
            'menu_items': 'Menu Items',
        }
        
    menu_name = forms.CharField()
    menu_active = forms.CheckboxInput()
    menu_items = CustomMMCF(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
    
   
    
   
    
    