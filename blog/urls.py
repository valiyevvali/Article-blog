from blog.views.category import category
from django.urls import path,include
from blog.views import home,category,myarticles

urlpatterns = [
    path('',home,name='home'),
    path('category/<slug:categorySlug>',category,name='category'),
    path('myarticles/',myarticles,name='myarticles')
]
