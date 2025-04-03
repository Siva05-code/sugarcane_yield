from django import forms
from .models import db

class SugarcaneYieldForm(forms.ModelForm):
    class Meta:
        model = db
        fields = ['historical_yield', 'rainfall', 'humidity', 'soil_ph', 'organic_content']
