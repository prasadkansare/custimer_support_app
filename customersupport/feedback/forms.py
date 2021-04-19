from django import forms
from .models import Feedback,Review
class FeedbackForm(forms.ModelForm):
    class Meta:  
        model = Feedback 
        fields = ['feedback']

        def clean(self):
            cleaned_data = super(FeedbackForm, self).clean()
            feedback = cleaned_data.get("feedback")
            return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:  
        model = Review 
        fields = ['review']

        def clean(self):
            cleaned_data = super(ReviewForm, self).clean()
            review = cleaned_data.get("review")
            return cleaned_data