from django.urls import path

from todolist.views import register, todolist, user_login, user_logout


app_name = 'todolist'
urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
