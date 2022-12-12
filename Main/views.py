from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Testimonial
from .forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        reviews = Testimonial.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categories"] = categories[:6]
        context["reviews"] = reviews
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


class PostView(ListView):
    model = Post
    template_name = "posts.html"
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add-post.html"

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


def CategoryListView(request):
    categories_list = Category.objects.all()
    return render(request, 'categories.html', {'categories_list':categories_list, 'category_navbar':categories_list, 'category_footer':categories_list})


def CategoryView(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category_id=category)
    return render(request, 'category-posts.html', {'posts':posts, 'category':category, 'category_navbar':categories, 'category_footer':categories[:4]})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update-post.html'

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('posts')

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add-comment.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(AddCommentView, self).get_context_data(*args, **kwargs)
        context["category_navbar"] = categories
        context["category_footer"] = categories[:4]
        return context

