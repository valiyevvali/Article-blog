from django import forms
from blog.models import ContactModel
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields='__all__'
    
   