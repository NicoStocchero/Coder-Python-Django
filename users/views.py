from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loguea al usuario automáticamente
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Sesión iniciada correctamente.")
            return redirect("profile")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "users/login.html")

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {
        'profile': request.user.profile
    })

@login_required
def profile_edit_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile, user=request.user)

    return render(request, 'users/profile_edit.html', {
        'form': form
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect("login")