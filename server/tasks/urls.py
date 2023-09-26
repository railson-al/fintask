from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', view=views.tasks),
    path('tasks/<str:pk>/', view=views.tasks_detail),
    path('tasks-status/', view=views.task_status),
    path('tasks-status/<str:pk>/', view=views.task_status_detail),
    path('categories/', view=views.categories),
    path('categories/<str:pk>/', view=views.categories_detail),
]