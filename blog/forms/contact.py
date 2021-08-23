from django import forms
from blog.models import ContactModel
from django.core.mail import send_mail
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        fields='__all__'
    def send_mail(self,mail,name):
        send_mail(
            subject='Article.com',
            message=f'Hörmətli {name } müraciətiniz qəbul olundu.Sizinlə tezliklə əlaqə saxlanılacaq.',
            from_email=None,
            recipient_list=[mail],
            fail_silently=False
        )
    
   