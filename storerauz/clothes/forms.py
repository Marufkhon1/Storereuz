from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'description', 'category', 'brand', 'price', 'size', 'color', 'image']

    # You can add additional form customization here if needed
