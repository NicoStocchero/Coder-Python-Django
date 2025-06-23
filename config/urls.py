"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    # Home
    index,
    # About
    about,
    # Posts
    post_list, post_detail, CreatePostView, PostEditView, PostDeleteView,
    # Autores
    AuthorListView, CreateAuthorView, AuthorEditView, AuthorDeleteView,
    # Categorías
    CategoryListView, CreateCategoryView, CategoryEditView, CategoryDeleteView,
    # Buscador
    search, result,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home
    path('', index, name='index'),
    
    # About
    path('about/', about, name='about'),
    
    # Buscador
    path('search/', search, name='search'),
    path('result/', result, name='result'),
    
    # Posts
    path('post/', post_list, name='post_list'),
    path('post/create/', CreatePostView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    
    # Autores
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/create/', CreateAuthorView.as_view(), name='author_create'),
    path('author/<int:pk>/edit/', AuthorEditView.as_view(), name='author_edit'),
    path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    # Categorías
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CreateCategoryView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryEditView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    
    # Users
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)