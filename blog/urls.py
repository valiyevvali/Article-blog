from django.urls import path,include
from blog.views import home,category,myarticles,detail_article,contact,add_article,edit_article,delete_article,delete_comment

urlpatterns = [
    path('',home,name='home'),
    path('category/<slug:categorySlug>',category.as_view(),name='category'),
    path('myarticles/',myarticles,name='myarticles'),
    path('article/<slug:articleSlug>',detail_article.as_view(),name='article_detail'),
    path('contact/',contact,name='contact'),
    path('add_article/',add_article,name='add_article'),
    path('edit/<slug:articleSlug>',edit_article,name='edit_article'),
    path('delete/<slug:articleSlug>',delete_article,name='delete_article'),
    path('delete_comment/<int:comment_id>',delete_comment,name='delete_comment'),
]
