from django import forms 
from .models import Shorter
 
class ShorterForm(forms.ModelForm):
    
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "輸入連結"}))
    
    class Meta:
        model = Shorter
 
        fields = ('long_url',)