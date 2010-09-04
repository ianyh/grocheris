from django import forms

from grocheris.models import GroceryItem

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ('name', 'locations')

    class Media:
        js = ('http://github.com/malsup/form/raw/master/jquery.form.js',)
