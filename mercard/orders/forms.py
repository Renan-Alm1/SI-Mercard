from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		products = kwargs.pop("products") or None
		super().__init__(*args, *kwargs)
		self.products = products
		
	class Meta:
		model = Order
		fields = [
			'shipping_address',
			'billing_address',
		]
		
	def clean(self, *args, **kwargs):
		cleaned_data = super().clean(*args, **kwargs)
		
		if self.products != None:
			if not self.products:
				raise forms.ValidationError("This product is out of inventory.")
		return cleaned_data