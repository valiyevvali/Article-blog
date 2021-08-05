from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import Register_Form
from django.contrib.auth import login,authenticate

def Register(request):
    if request.method == 'POST':
        form=Register_Form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Welcome...')
            return redirect('home')
    else:
        form=Register_Form()
    context={
        'form':form
    }
    return render(request,'pages/register.html',context)