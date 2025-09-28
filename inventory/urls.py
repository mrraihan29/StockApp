from django.urls import path
from . import views

urlpatterns = [
    # Ketika seseorang mengunjungi URL utama aplikasi ini (''),
    # panggil fungsi 'login_view' dari views.py
    # Kita beri nama rute ini 'login' untuk pemanggilan di masa depan.
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
