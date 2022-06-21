from email.policy import default
from django import forms
from .models import MenuItem, Menu

class CustomMMCF(forms.ModelMultipleChoiceField):
    
    def label_from_instance(self, menuitem):
        return  str(menuitem)
    
class CreateMenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ['name', 'active', 'starters', 'mains', 'deserts', 'drinks', 'sides']
        labels = {
            'name': 'Name',
            'active': 'Active',
            'starters': 'Starters',
            'mains': 'Mains',
            'deserts': 'Deserts',
            'drinks': 'Drinks',
            'sides': 'Sides'
        }
        
    name = forms.CharField()
    active = forms.CheckboxInput()
    starters = CustomMMCF(
        queryset=MenuItem.objects.filter(type='starter'),
        widget=forms.CheckboxSelectMultiple()
    )
    mains = CustomMMCF(
        queryset=MenuItem.objects.filter(type='main'),
        widget=forms.CheckboxSelectMultiple()
    )
    deserts = CustomMMCF(
        queryset=MenuItem.objects.filter(type='desert'),
        widget=forms.CheckboxSelectMultiple()
    )
    drinks = CustomMMCF(
        queryset=MenuItem.objects.filter(type='drink'),
        widget=forms.CheckboxSelectMultiple()
    )
    sides = CustomMMCF(
        queryset=MenuItem.objects.filter(type='side'),
        widget=forms.CheckboxSelectMultiple()
    )
    
    
   
    
   
    
    