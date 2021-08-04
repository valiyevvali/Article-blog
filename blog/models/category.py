from enum import unique
from django.db import models
from autoslug import AutoSlugField
class CategoryModel(models.Model):
    name=models.CharField(max_length=30,blank=False,null=False)
    slug=AutoSlugField(populate_from='name',unique=True)

    class Meta:
        db_table='Category'
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name