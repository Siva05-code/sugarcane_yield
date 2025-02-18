from django import forms
from .models import SugarcaneYield

class SugarcaneYieldForm(forms.ModelForm):
    class Meta:
        model = SugarcaneYield
        fields = ['historical_yield', 'rainfall', 'humidity', 'soil_ph', 'organic_content']
