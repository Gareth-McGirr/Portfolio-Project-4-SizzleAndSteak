from django import forms
from .models import MenuItem, Menu


class CustomMMCF(forms.ModelMultipleChoiceField):
    """
    Get custom menu item name labels for checkboxes
    """
    def label_from_instance(self, menuitem):
        """
        Returns labels
        """
        return str(menuitem)


class CreateMenuForm(forms.ModelForm):
    """
    Form to edit and delete menus
    """
    class Meta:
        """
        Define model, form fields and label
        """
        model = Menu
        fields = [
            'name', 'active', 'starters', 'mains',
            'deserts', 'drinks', 'sides'
        ]

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


class CreateMenuItemForm(forms.ModelForm):
    """ Create MenuItem form """
    class Meta:
        """ Define model, fiels and labels """
        model = MenuItem
        fields = [
            'name', 'type', 'description', 'price',
            'contains_nuts', 'vegetarian', 'vegan',
            'gluten_free'
        ]
