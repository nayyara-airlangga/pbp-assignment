from django.urls import path

from todolist.views import (
    create_task,
    delete_task,
    register,
    todolist,
    update_status,
    user_login,
    user_logout,
)


app_name = 'todolist'
urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-task', create_task, name='create_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]
