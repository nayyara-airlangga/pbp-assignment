from django.urls import path

from todolist.views import (
    add_task,
    create_task,
    delete_task,
    register,
    todolist,
    todolist_json,
    update_status,
    user_login,
    user_logout,
)


app_name = 'todolist'
urlpatterns = [
    path('', todolist, name='todolist'),
    path('json', todolist_json, name='todolist_json'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create-task', create_task, name='create_task'),
    path('add', add_task, name='add_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
]
