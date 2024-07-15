# wardrobe/forms.py
from django import forms
from .models import WardrobeItem


class WardrobeItemCreateForm(forms.ModelForm):
    class Meta:
        model = WardrobeItem
        fields = ['brand', 'material', 'image']  # Exclude name, category, and color

