from django.core import paginator
from django.shortcuts import render,get_object_or_404
from blog.models import ArticleModel,CategoryModel
from django.core.paginator import Paginator
from django.views.generic import ListView


class category(ListView):
    model=CategoryModel
    template_name='pages/category.html'
    context_object_name='articles'
    paginate_by=1

    def get_queryset(self):
        category_name=get_object_or_404(CategoryModel,slug=self.kwargs['categorySlug'])
        return category_name.text.all()
        

# def category(request,categorySlug):
#     category_name=get_object_or_404(CategoryModel,slug=categorySlug)
#     articles=category_name.text.all()
#     page=request.GET.get('page')
#     paginator=Paginator(articles,1)
#     return render(request,'pages/category.html',context={
#         'articles':paginator.get_page(page),
#         'category_name':category_name.name
#         })
    