from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    picture=models.ImageField(upload_to='user_pictures/',blank=True,null=True)

    class Meta:
        db_table='User'
        verbose_name='user'
        verbose_name_plural='Users'
    
    def __str__(self):
        return self.username
