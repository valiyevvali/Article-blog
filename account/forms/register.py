from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from account.models import CustomUserModel
class Register_Form(UserCreationForm):

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