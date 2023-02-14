from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    succes_url = '/'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    # def get_success_url(self):
    #    return '/'

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
   # queryset = Article.objects.all() # <blog>/<modelname>_list.html
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
    

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    succes_url = '/'
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
# class ArticleDeleteView(DeleteView):
#     template_name = 'articles/article_delete.html'
#    # queryset = Article.objects.all() # <blog>/<modelname>_list.html
    
#     def get_object(self):
#         id = self.kwargs.get("id")
#         obj = get_object_or_404(Article, id=id)
#         if(obj):
#             if(obj.delete()):
#               return redirect('../../')

    
#     def get_success_url(self):
#         return reverse('articles:article-list')
    
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
   # queryset = Article.objects.all() # <blog>/<modelname>_list.html
    
    def get_object(self):
        id = self.kwargs.get("id")
        obj = get_object_or_404(Article, id=id)
        if(obj):
            if(obj.delete()):
              return redirect('../../')

    
    def get_success_url(self):
        return reverse('articles:article-list')
    