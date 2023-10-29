from django.urls import path
from base import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard')
]
