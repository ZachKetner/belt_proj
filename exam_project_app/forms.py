from socket import fromshare
from django import forms
from .models import Quotes

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ('author', 'description')
    
