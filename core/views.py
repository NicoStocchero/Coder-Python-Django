from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post

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
    return render(request, 'core/search.html')

def result(request):
    query = request.GET.get('consulta', '').strip()
    if not query:
        messages.warning(request, 'Ingresá un término para buscar.')
        return redirect('search')

    resultados = Post.objects.filter(title__icontains=query)
    return render(request, 'core/result.html', {
        'query': query,
        'resultados': resultados,
    })