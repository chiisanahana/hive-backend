from django import forms
from .models import Car
from .models import CarFile

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('brand', 'year', 'color', 'seat', 'vehicle_no', 'transmission', 'price', 'deposit', 'description', 'status', 'provider_id')
        # fields = '__all__'

class CarFileForm(forms.Form):
    file = forms.FileField()
        
class ManualCarForm(forms.Form):
    # provider_id = forms.HiddenInput()
    brand = forms.CharField(max_length=20)
    year = forms.CharField(max_length=4)
    color = forms.CharField(max_length=20)
    seat = forms.IntegerField(min_value=1)
    vehicle_no = forms.CharField(max_length=15)
    transmission = forms.CharField(max_length=10)
    price = forms.FloatField()
    deposit = forms.FloatField(required=0)
    description = forms.CharField(required=0)
    
    # status = forms.CharField()
    # created_datetime = forms.DateTimeField(auto_now_add=True)
    # updated_datetime = forms.DateTimeField(auto_now=True)
        