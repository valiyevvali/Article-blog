from django.contrib.auth import logout
from django.shortcuts import redirect
def Logout_user(request):
    logout(request)
    return redirect('home')