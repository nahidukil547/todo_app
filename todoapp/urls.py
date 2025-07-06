from django.urls import path
from . import views
urlpatterns = [
    # for todo list modify 
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
    # for registration and login
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]