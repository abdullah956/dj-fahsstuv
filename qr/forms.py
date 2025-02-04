from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    issue_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )
    valid_until = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )
    class Meta:
        model = Certificate
        fields = '__all__'
