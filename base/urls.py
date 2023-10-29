from django.urls import path
from base import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path(
        'change-password/', views.CustomPasswordChangeView.as_view(),
        name='password_change'
    ),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path(
        'courses/create/', views.CourseCreateView.as_view(),
        name='course_create'
    ),
    path(
      'courses/<int:pk>/update/',views.CourseUpdateView.as_view(),
      name='course_update'
    ),
    path(
      'courses/<int:pk>/delete/', views.CourseDeleteView.as_view(),
      name='course_delete'
    ),

]
