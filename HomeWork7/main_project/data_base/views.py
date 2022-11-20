from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import *
from .filters import PostFilter

class NewsList(ListView):
    model = Post
    ordering = '-time_of_addition'
    template_name = 'news.html'
    context_object_name = 'news_all'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsSearchList(ListView):
    model = Post
    ordering = '-time_of_addition'
    template_name = 'news_search.html'
    context_object_name = 'news_all'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class News_oneDetail(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news'

class ArticleList(ListView):
    model = Post
    ordering = '-time_of_addition'
    template_name = 'article.html'
    context_object_name = 'post_all'

class CategoryList(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

class CategoryCreate(CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category_edit.html'

class CategoryUpdate(UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category_edit.html'

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        npost = form.save(commit=False)
        npost.type = 'news'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        npost = form.save(commit=False)
        npost.type = 'article'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article')