from django.forms.models import ModelForm
from .models import Brand, Product


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'category']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'brand']