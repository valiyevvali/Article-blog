from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel

class ProfileEditForm(UserChangeForm):
    password=None
    class Meta:
        model=CustomUserModel
        fields=('email','first_name','last_name','picture')