from django.db import models

class DateAbstract(models.Model):
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True