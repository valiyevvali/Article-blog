from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
@login_required(login_url='/')
def Change_Password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            this_user=form.save()
            update_session_auth_hash(request,this_user)
            messages.info(request,'Password has been change succesfuly...')
            return redirect('change_password')
    else:
        form=PasswordChangeForm(request.user)
    context={
        'form':form
    }
    return render(request,'pages/change_password.html',context)