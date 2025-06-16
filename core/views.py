from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post, Author, Category

def index(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html',{'posts': posts})

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado correctamente')
            return redirect('/')
        else:
            messages.error(request, 'Error al crear el post')
    else:
        form = PostForm()
    
    return render(request, 'core/post.html', {'form': form})

def search(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/search.html', {
        'authors': authors,
        'categories': categories,
    })

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
        results = results.filter(author_id=author_id)
        if author_id:
            try:
                author_obj = Author.objects.get(id=author_id)
            except Author.DoesNotExist:
                author_obj = None
    if category_id:
        results = results.filter(category_id=category_id)
        if category_id:
            try:
                category_obj = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                category_obj = None

    return render(request, 'core/result.html', {
        'query': query,
        'results': results,
        'author': author_obj,
        'category': category_obj,
    })