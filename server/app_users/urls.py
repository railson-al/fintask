from django.urls import path

from app_users import views

urlpatterns = [
    path('users/', views.UserView.user_auth, name='users-test')
]