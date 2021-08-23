from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from account.forms import Register_Form
from django.contrib.auth import login,authenticate
from django.core.mail import EmailMessage
from django.views import View
from django.urls import reverse
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from account.utils import token_generator

from django.contrib.auth import get_user_model
def Register(request):
    if request.method == 'POST':
        form=Register_Form(request.POST)
        if form.is_valid() :
            send_to=form.cleaned_data.get('email')
            user=form.save(commit=False)
            user.is_active=False
            user.save()

            # username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password1')
            # user=authenticate(username=username,password=password)
            # login(request,user)
            domain=get_current_site(request).domain
            uidb64=urlsafe_base64_encode(force_bytes(user.pk))
            link=reverse('activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
            activate_url='http://'+domain+link
            email_subject='Activate your account...'
            email_body='Hi ' + user.username + '\n Please use this link to verify your account.\n' +activate_url

            email = EmailMessage(
                email_subject,
                email_body,
                'valiyevvali101@gmail.com',
                [send_to],
                ['bcc@example.com'],
            )
            email.send(fail_silently=False)

            messages.success(request,'Thanks for your registration, please check your inbox!')
            return redirect('register')
    else:
        form=Register_Form()
    context={
        'form':form
    }
    return render(request,'pages/register.html',context)

def Verification(request,uidb64,token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.<a href="/account/login">Login<a>')
    else:
        return HttpResponse('Activation link is invalid!')

  