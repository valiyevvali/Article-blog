from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfileEditForm
@login_required(login_url='/')
def Edit_Profile(request):
    if request.method == 'POST':
        form=ProfileEditForm(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Changes are added...')
            return redirect('profile_edit')
    else:
        form=ProfileEditForm(instance=request.user)
    context={
        'form':form
    }
    return render(request,'pages/profile_edit.html',context)