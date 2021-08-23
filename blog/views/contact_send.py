from django.shortcuts import redirect, render
from blog.forms import ContactForm
from blog.models import ContactModel
from django.contrib import messages
from django.core.mail import send_mail
def contact(request):
    form=ContactForm(
        # data={
        #     'email':'valiyevveli@outlook.com'
        # }
        # initial={
        #     'email':'valiyevveli@outlook.com'
        # }
    )
    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail(form.cleaned_data.get('email'),form.cleaned_data.get('name_surname'))
            messages.info(request, 'Your message has been sent successfully...')
            return redirect('contact')
    context={
        'form':form
    }
    return render(request,'pages/contact.html',context)
   