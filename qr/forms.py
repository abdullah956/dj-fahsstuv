from django import forms
from .models import Certificate
class CertificateForm(forms.ModelForm):
    issue_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )
    valid_until = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        input_formats=["%Y-%m-%d"]
    )

    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
           "id_no": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "s_office": forms.TextInput(attrs={"class": "form-control"}),  # Added missing field
            "ts_no": forms.TextInput(attrs={"class": "form-control"}),  # Added missing field
            "company": forms.TextInput(attrs={"class": "form-control"}),  # Added missing field
            "id_iqama_no": forms.TextInput(attrs={"class": "form-control"}),
            "details": forms.Textarea(attrs={"class": "form-control", "rows": 4}),  # Added rows for better UI
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }







