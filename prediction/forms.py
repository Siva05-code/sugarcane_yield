from django import forms
from .models import first

class SugarcaneYieldForm(forms.ModelForm):
    class Meta:
        model = first
        fields = ['historical_yield', 'rainfall', 'humidity', 'soil_ph', 'organic_content']
