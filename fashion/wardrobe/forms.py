# wardrobe/forms.py
from django import forms
from .models import WardrobeItem

class WardrobeItemForm(forms.ModelForm):
    class Meta:
        model = WardrobeItem
        fields = '__all__'

