from django import forms
from .models import Product,UserProfile

class ProductForm(forms.ModelForm):
    model = Product
    fields = '__all__'

class UserProfileForm(forms.ModelForm):
    model = UserProfile
    fields = '__all__'

