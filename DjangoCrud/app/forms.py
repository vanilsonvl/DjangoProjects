from django.forms.models import ModelForm

from app.models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'year', 'value', 'register_date']