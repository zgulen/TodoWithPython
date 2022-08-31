from django.contrib import admin
from django.urls import path,include
from .views import home,todo_create, todo_delete, todo_update

urlpatterns = [
    path('', home,name='home'),
    path('add', todo_create, name='add'),
    path('update/<int:id>', todo_update, name='update'),
    path('delete/<int:id>', todo_delete, name='delete'),
    ]