from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserView.user_auth, name='users-test')
]