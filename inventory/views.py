from django.shortcuts import render, redirect
# Import fungsi autentikasi bawaan dari django
from django.contrib.auth import authenticate, login, logout
# Import sistem pesan Django untuk menampilkan pesan error
from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.

# Ini adalah 'view' untuk halaman login
# Sekarang tugasnya hanya merender template login.html
def login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        user = authenticate(request, username=username_input, password=password_input)
        if user is not None:
            login(request, user)
            return redirect('dashboard') # Gunakan redirect di sini
        else:
            messages.error(request, 'Username atau password salah!')
    return render(request, 'inventory/login.html')

def logout_view(request):
    # Panggil fungsi logout bawaan Django
    logout(request)
    # Redirect pengguna ke halaman login
    return redirect('login')

@login_required
def dashboard(request):
  return render(request, 'inventory/dashboard.html')