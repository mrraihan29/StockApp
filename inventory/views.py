from django.shortcuts import render

# Create your views here.

# Ini adalah 'view' untuk halaman login
# Sekarang tugasnya hanya merender template login.html
def login_view(request):
  # Fungsi render() mengambil request dari pengguna dan...
  # file template HTML, lalu menggabungkannya menjadi halaman web
  return render(request, 'inventory/login.html')