from django.urls import path

from app_users import views

urlpatterns = [
    path('users/', views.users_view, name='users'),
    path('users/login/', views.user_authenticate, name='users_login'),

    path('sectors/', views.sectors, name='sector'),
]