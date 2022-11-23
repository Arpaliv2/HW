from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Category
from .forms import *
from .filters import PostFilter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives, mail_managers
from main_project.settings import SERVER_EMAIL
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Post)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        users = []
        for i in post.category:
            for j in i.subscribers:
                users.append(j)
        users = set(users)
        mail_args = Post(
            heading=post.heading,
            text=post.text[:50],
        )
        for user in users:
            html_content = render_to_string(
                'news_mail.html',
                {
                    'username': user.username,
                    'text': mail_args.text,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'{mail_args.heading}',
                body=mail_args.text,
                from_email=SERVER_EMAIL,
                to=[user.email]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()


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

class CategoryCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('data_base.add_Category')
    form_class = CategoryForm
    model = Category
    template_name = 'category_edit.html'

class CategoryUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('data_base.change_Category')
    form_class = CategoryForm
    model = Category
    template_name = 'category_edit.html'

class NewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('data_base.add_Post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        npost = form.save(commit=False)
        npost.type = 'news'
        return super().form_valid(form)

class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('data_base.add_Post')
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        npost = form.save(commit=False)
        npost.type = 'article'
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('data_base.change_Post')
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

class ArticleUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('data_base.change_Post')
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

class NewsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('data_base.delete_Post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')

class ArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('data_base.delete_Post')
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article')