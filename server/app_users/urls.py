from django.urls import path

from app_users import views

urlpatterns = [
    path('users/', views.users_view, name='users-list')
]