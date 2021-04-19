from django import forms
from .models import Enquiry
from django.core.validators import RegexValidator

class EnquiryForm(forms.ModelForm):
    # mobile = forms.CharField(min_length=10,required=True)
    class Meta:  
        model = Enquiry  
        fields = ['name','mobile','email','query']

        def clean(self):
            cleaned_data = super(EnquiryForm, self).clean()
            name = cleaned_data.get("name")
            mobile = cleaned_data.get("mobile")
            email = cleaned_data.get("email")
            query = cleaned_data.get("query")
            print("query",query)

            return cleaned_data