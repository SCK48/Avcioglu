from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Select, NumberInput

from product.models import Order

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'product', 'quantity', 'note']