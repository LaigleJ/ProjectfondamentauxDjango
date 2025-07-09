from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['job', 'rating', 'comment', 'author']  # adapte selon ton modèle

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is None or not (1 <= rating <= 5):
            raise forms.ValidationError("La note doit être comprise entre 1 et 5.")
        return rating
