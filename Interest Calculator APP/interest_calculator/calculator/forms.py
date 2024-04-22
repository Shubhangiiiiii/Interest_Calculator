from django import forms
from .models import InterestCalculation

class InterestCalculationForm(forms.ModelForm):
    class Meta:
        model = InterestCalculation
        fields = ['principal_amount', 'interest_rate', 'time_period']