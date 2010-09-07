from django import forms

from grocheris.models import GroceryItem, Location

class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ('name', 'locations')

class LocationSelectionForm(forms.Form):
    locations = forms.ModelChoiceField(queryset=Location.objects.all(), 
                                       empty_label=None)

class TagForm(forms.Form):
    name = forms.CharField(max_length=50)
