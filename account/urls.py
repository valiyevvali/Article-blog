from django.urls import path,include
from account.views import Logout_user,Change_Password,Edit_Profile,Register
urlpatterns = [
   path('logout',Logout_user,name='logout'),
   path('change_password',Change_Password,name='change_password'),
   path('profile_edit',Edit_Profile,name='profile_edit'),
   path('register',Register,name='register'),
]
