from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django import forms
from account.models import CustomUserModel
from django.core.exceptions import ValidationError
class Register_Form(UserCreationForm):
    email = forms.EmailField(required=True, max_length=150)
    class Meta:
        model=CustomUserModel
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUserModel.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
      