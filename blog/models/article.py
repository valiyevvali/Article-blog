
from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel 
from .abstract_model import DateAbstract
class ArticleModel(DateAbstract):
    header=models.CharField(max_length=50)
    content=models.TextField()
    slug=AutoSlugField(populate_from='header',unique=True)
    categories=models.ManyToManyField(CategoryModel,related_name='text')
    author=models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='texts')
    picture=models.ImageField(upload_to='article_images')

    class Meta:
        db_table='Article'
        verbose_name_plural='Articles'
        verbose_name='article'
    
    def __str__(self):
        return self.slug