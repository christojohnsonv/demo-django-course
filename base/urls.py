from django.urls import path
from base import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path(
        'change-password/', views.CustomPasswordChangeView.as_view(),
        name='password_change'
    ),
    path('short-course-view/', views.ShortCourseView.as_view(), name='short-course-view')
]
