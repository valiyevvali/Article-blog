from django.db import models

class ContactModel(models.Model):
    email=models.EmailField(max_length=250)
    name_surname=models.CharField(max_length=60)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Contact'
        verbose_name='contact'
        verbose_name_plural='Contacts'
        
    def __str__(self):
        return self.email