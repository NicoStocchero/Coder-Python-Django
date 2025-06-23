from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import PostForm, AuthorForm, CategoryForm
from .models import Post, Author, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Home
def index(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html',{'posts': posts})

# About
def about(request):
    return render(request, 'core/about.html')

# Reusable views
class BaseListView(LoginRequiredMixin, ListView):
    success_url = reverse_lazy('index')

class BaseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy('index')

class BaseEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_url = reverse_lazy('index')

class BaseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    success_url = reverse_lazy('index')


# Post
class CreatePostView(BaseCreateView):
    model = Post
    form_class = PostForm
    template_name = 'core/post/post_form.html'
    success_message = "Post creado correctamente"

class PostEditView(BaseEditView):
    model = Post
    form_class = PostForm
    template_name = 'core/post/post_form.html'
    success_message = "Post actualizado correctamente"

class PostDeleteView(BaseDeleteView):
    model = Post
    template_name = 'core/post/post_delete.html'
    success_message = "Post eliminado correctamente"

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'core/post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'core/post/post_detail.html', {'post': post})

# Author
class CreateAuthorView(BaseCreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'core/author/author_form.html'
    success_message = "Autor creado correctamente"

class AuthorEditView(BaseEditView):
    model = Author
    form_class = AuthorForm
    template_name = 'core/author/author_form.html'
    success_message = "Autor actualizado correctamente"

class AuthorDeleteView(BaseDeleteView):
    model = Author
    template_name = 'core/author/author_delete.html'
    success_message = "Autor eliminado correctamente"

class AuthorListView(BaseListView):
    model = Author
    template_name = 'core/author/author_list.html'
    context_object_name = 'authors'

# Category
class CreateCategoryView(BaseCreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'core/category/category_form.html'
    success_message = "Categoría creada correctamente"

class CategoryEditView(BaseEditView):
    model = Category
    form_class = CategoryForm
    template_name = 'core/category/category_form.html'
    success_message = "Categoría actualizada correctamente"

class CategoryDeleteView(BaseDeleteView):
    model = Category
    template_name = 'core/category/category_delete.html'
    success_message = "Categoría eliminada correctamente"

class CategoryListView(BaseListView):
    model = Category
    template_name = 'core/category/category_list.html'
    context_object_name = 'categories'

# Search
def search(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/search.html', {
        'authors': authors,
        'categories': categories,
    })

# Result
def result(request):
    query = request.GET.get('query', '').strip()
    author_id = request.GET.get('author')
    category_id = request.GET.get('category')

    results = Post.objects.all()

    author_obj = None
    category_obj = None

    if query:
        results = results.filter(title__icontains=query)
    if author_id:
        try:
            author_obj = Author.objects.get(id=int(author_id))
            results = results.filter(author=author_obj)
        except (ValueError, Author.DoesNotExist):
            author_obj = None

    if category_id:
        try:
            category_obj = Category.objects.get(id=int(category_id))
            results = results.filter(category=category_obj)
        except (ValueError, Category.DoesNotExist):
            category_obj = None

    return render(request, 'core/result.html', {
        'query': query,
        'results': results,
        'author': author_obj,
        'category': category_obj,
    })

