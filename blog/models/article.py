from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel 
class ArticleModel(models.Model):
    header=models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    slug=AutoSlugField(populate_from='header',unique=True)
    categories=models.ManyToManyField(CategoryModel,related_name='text')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='texts')
    picture=models.ImageField(upload_to='article_images')

    class Meta:
        db_table='Article'
        verbose_name_plural='Articles'
        verbose_name='article'
    
    def __str__(self):
        return self.slug