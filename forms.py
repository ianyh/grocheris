from django import forms

from grocheris.models import GroceryItem

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ('name', 'location')
