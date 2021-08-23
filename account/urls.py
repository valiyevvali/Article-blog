from django.urls import path,include
from account.views import Logout_user,Change_Password,Edit_Profile,Register,Verification
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('login',auth_views.LoginView.as_view(
      template_name='registration/login.html'
   ),name='login_user'),
   path('logout',Logout_user,name='logout_user'),
   path('change_password',Change_Password,name='change_password'),
   path('profile_edit',Edit_Profile,name='profile_edit'),
   path('register',Register,name='register'),
   path('activate/<uidb64>/<token>',Verification,name='activate'),
   path('password_reset/',auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
   path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
   path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),      
]
