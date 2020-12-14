from django import forms

from .models import Products

class ProductsForm(forms.ModelForm):
   
   class Meta:
        model = Products
        fields = [
            'title',
            'price',
            'images',
            'tipo',
            'country',
            'quantity',
            'Language',
            'Card_condition',
            'Game_condition',

        ]

