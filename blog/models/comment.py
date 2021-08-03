from django.db import models
from blog.models import ArticleModel
from .abstract_model import DateAbstract
class CommentModel(DateAbstract):
    author=models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE,related_name='yorum')
    article=models.ForeignKey(ArticleModel,on_delete=models.CASCADE,related_name='yorumlar')
    comment=models.TextField()

    class Meta:
        db_table='Comment'
        verbose_name='comment'
        verbose_name_plural='Comments'
    def __str__(self):
        return self.comment