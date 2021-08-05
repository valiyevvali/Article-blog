from django import forms
from django.forms import widgets,Textarea
from django.forms.fields import CharField
from blog.models import CommentModel
class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=('comment',)
    
   
   
   