from django.db import models
from django.contrib.auth.models import User
from blog.models import ArticleModel
class CommentModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='yorum')
    article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE,related_name='yorumlar')
    comment=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    class Meta:
        db_table='Comment'
        verbose_name='comment'
        verbose_name_plural='Comments'
    def __str__(self):
        return self.comment