# Assignment 4: Implementing Forms and Authentication Using Django

[Link to Site]: https://pbp-web-assignment.herokuapp.com
[site]: https://pbp-web-assignment.herokuapp.com

[Link to Site]

## Why do we use the `{% csrf_token %}` in our `<form>` element? What happens if we remove it?

Firstly, let's see what CSRF is. CSRF or Cross Site Request Forgery attack is an exploit which makes a trusted user do unwanted actions on a web application in
which these users have been authenticated properly.

The `{% csrf_token %}` tag is Django's way of protecting against CSRF attacks. It's usage in forms is as simple as adding it inside of our `<form>`. When we generate a page
from the server side to render/send, the `{% csrf_token %}` tag generates a token which will be used to verify/check incoming requests. Requests that don't have this token
will not be executed. The `django.middleware.csrf.CsrfViewMiddleware`, a CSRF middleware, is activated which serves as a mechanism to ensure that we implement CSRF
verification by using the `{% csrf_token %}` tag in forms for example. Attempting to make a request to a form without the `{% csrf_token %}` will return a 403 Forbidden error
with a message stating `CSRF verification failed`.

## Can we make a `<form>` manually without generators? If we can, how to do it manually?

It's definitely possible. We just need the `<form>` tag to start. Depending on what we want to do, we have to set the method of the form (e.g. `<form method="POST">`).
We then add the `{% csrf_token %}` inside of our `<form>` to ensure CSRF verification. To get user input, we add the appropriate `<input>` and other input related tags to
our form. We then add a submit button which will submit the form as the name imply (`<button type="submit">`). When a view receives the request, we can get the form data by
utilizing its method to get the input (e.g. `request.POST.get("name")`).

## How is the flow from data submission via forms, saving data to the database, until we show the data in an HTML template?

When a form is submitted, its essentially sending a request to our server in which the body is the user input. This request method depends on the form's method. Let's say
its a POST request for simplicity. A view that receives the request can get the user input via its request method (e.g. accessing the `name` attribute 
via `request.POST.get("name")`). If our form is a `ModelForm` we can use its `save` method to create an instance/data from that form. Alternatively, we could also use the
appropriate model's `create` method with the form's data as its arguments. Once the data is saved to the database, we can get that data from a view by using various methods 
available to the corresponding model (e.g. `Model.objects.all`, `Model.objects.filter`, `Model.objects.filter`). To render the data in an HTML template, we pass the data as 
part of a context for the template which we can then use from within the HTML template using the appropriate tags.

## Implementing the checklists

Note: The steps for the bonus implementation is not written here. It will be explained in the demos if its all right.

1. Create the `todolist` app if we haven't already.

    ```bash
    python manage.py startapp todolist
    ```
    
2. Add `todolist` to `INSTALLED_APPS` in `project_django/settings.py`.

    ```python
    INSTALLED_APPS = [
        # ...
        'todolist',
    ]
    ```

3. Create the `Task` model.

    ```python
    from typing import Iterable, Optional
    from django.utils import timezone
    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
    class Task(models.Model):
        user = models.ForeignKey(to=User, on_delete=models.CASCADE)
        date = models.DateField(default=timezone.now)
        title = models.CharField(max_length=255)
        description = models.TextField()
    ```
  
    Once the model is created, run `python manage.py makemigrations` to make migrations for the new model and `python manage.py migrate` to apply the migrations to the
    database.
    
4. Create the necessary view functions in `todolist/views.py`.

    ```python
    from datetime import datetime
    from django.contrib.auth import authenticate, login, logout
    from django.http.response import HttpResponseRedirect
    from django.shortcuts import redirect, render
    from django.contrib import messages
    from django.contrib.auth.decorators import login_required
    from django.contrib.auth.forms import UserCreationForm
    from django.urls import reverse

    from todolist.forms import CreateTaskForm
    from todolist.models import Task

    # Create your views here.
    @login_required(login_url='/todolist/login')
    def todolist(request):
        tasks = Task.objects.filter(user=request.user.pk)

        return render(
            request, 'todolist.html', context={'user': request.user, 'tasks': tasks}
        )


    @login_required(login_url='/todolist/login')
    def create_task(request):
        form = CreateTaskForm()

        if request.method == "POST":
            form = CreateTaskForm(request.POST)

            if form.is_valid():
                form.save(request.user.id)
                messages.success(request, 'Task added successfully!')
                return redirect('todolist:todolist')

        context = {'form': form}
        return render(request, 'create-task.html', context)


    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been created succesfully!')
                return redirect('todolist:login')

        context = {'form': form}

        return render(request, 'register.html', context)


    def user_login(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                res = HttpResponseRedirect(reverse('todolist:todolist'))
                res.set_cookie('last_login', str(datetime.now()))

                return res
            else:
                messages.info(request, 'Incorrect username or password!')

        return render(request, 'login.html')


    def user_logout(request):
        if request.method == "POST":
            logout(request)
            res = HttpResponseRedirect(reverse('todolist:login'))
            res.delete_cookie('last_login')
            return res

        return render(request, 'logout.html', context={'user': request.user})
    ```
    
5. Add a `todolist/` path in the `urlpatterns` of `project_django/urls.py`. It will add a `/todolist` route from the base path.

   ```python
   urlpatterns = [
       # ...
       path('todolist/', include('todolist.urls')),
   ]
   ```
   
6. Create a `urls.py` in `todolist` and add the `app_name` and `urlpatterns` and add the respective handlers according to the path name and use cases.

    ```python
    from django.urls import path

    from todolist.views import create_task, register, todolist, user_login, user_logout


    app_name = 'todolist'
    urlpatterns = [
        path('', todolist, name='todolist'),
        path('register/', register, name='register'),
        path('login/', user_login, name='login'),
        path('logout/', user_logout, name='logout'),
        path('create-task', create_task, name='create_task'),
    ]
    ```
    
7. Create the appropriate templates.

    - `todolist.html`
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Todolist - My Tasks</title>
        {% endblock meta %}

        {% block content %}

        <h1>{{ user.username }}'s Tasks</h1>
        <a href="{% url 'todolist:create_task' %}"><button>New Task</button></a></td>
        <a href="{% url 'todolist:logout' %}"><button>Logout</button></a></td>

        <table style="margin-top: 20px; text-align: center;">  
          <tr style="font-size: 18px;">
            <th>Title</th>
            <th>Created At</th>
            <th>Description</th>
          </tr>
         {% for task in tasks %}
         <tr style="text-align: left;">
           <td>{{ task.title }}</td>
           <td>{{ task.date }}</td>
           <td>{{ task.description }}</td>
         </tr>
         {% endfor %}
       </table>

       {% if messages %}
         <ul>
           {% for message in messages %}
           <li>{{ message }}</li>
           {% endfor %}
         </ul>
       {% endif %}

       {% endblock content %}
        ```
        
    - `register.html`

        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Todolist - Register</title>
        {% endblock meta %}

        {% block content %}

        <div class="register">

          <h1>Registration Form</h1>

          <form method="POST" action="">
            {% csrf_token %}
            <table>
              {{ form.as_table }}
              <tr>
                <td></td>
                <td style="margin-bottom: 10px;"><input type="submit" name="submit" value="Register" /></td>
              </tr>
            </table>
          </form>

          {% if messages %}
            <ul>
              {% for message in messages %}
                <li>{{ message }}</li>
              {% endfor %}
            </ul>
          {% endif %}

          Already have an account? <a href="{% url 'todolist:login' %}">Login</a>

        </div>

        {% endblock content %}
        ```
        
    - `login.html`
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Todolist - Login</title>
        {% endblock meta %}

        {% block content %}

        <div class="login">

          <h1>Login Form</h1>

          <form method="POST" action="">
            {% csrf_token %}
            <table>
              <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
              </tr>

              <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
              </tr>

              <tr>
                  <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
              </tr>
            </table>
          </form>

          {% if messages %}
          <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
          </ul>
          {% endif %}

          Don't have an account? <a href="{% url 'todolist:register' %}">Register</a>

        </div>

        {% endblock content %}
        ```
        
    - `logout.html`
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Todolist - Logout</title>
        {% endblock meta %}

        {% block content %}

        <div class="logout">

          <h1>Logout</h1>

          {% if user.username %}
          <p>You are currently logged in as <strong>{{ user.username }}</strong></p>
          {% else %}
          <p>You are currently not logged in as anyone</p>
          {% endif %}

          <form method="POST" action="">
            {% csrf_token %}
            <table>
              <tr>
                <td style="padding-bottom: 10px;">Are you sure you want to logout?</td>
              </tr>
              <tr>
                <td><input class="btn logout_btn" type="submit" value="Logout"></td>
              </tr>
            </table>
          </form>
        </div>

        {% endblock content %}
        ```
        
    - `create-task.html`
    
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Todolist - Create New Task</title>
        {% endblock meta %}

        {% block content %}
        <div>

        <h1>Create new task</h1>

        <form method="POST" action="">
          {% csrf_token %}
          <table>
            {{ form.as_table }}
            <tr>
              <td></td>
              <td style="margin-bottom: 10px;"><input type="submit" name="submit" value="Create" /></td>
            </tr>
          </table>
        </form>

        </div>
        {% endblock content %}
        ```
        
7. Deploy the site to Heroku.

    - Create a new Heroku app.
    - Go to the created app's settings and set the `HEROKU_APP_NAME` config variable to match the created Heroku app's name.
    - Go to our account settings and copy our Heroku API key.
    - Set repository secrets in our GitHub repository.
      - Navigate to `Settings -> Secrets -> Actions`.
      - Create two repository secrets.
        - `HEROKU_APP_NAME`: Name of your Heroku app
        - `HEROKU_API_KEY`: Your Heroku API key
    - Push our changes in the previous steps to trigger the GitHub `dpl.yml` workflow.
    - Alternatively, if our changes have been pushed before setting the secrets, once we set the secrets, go to the `Actions` tab and click on the the failed workflow and select `Run/Re-run all jobs`.
    - Wait until the workflow finish running.
    - Congratulations! Your Django site is up and running!

8. Create a `superuser` for our Heroku site using the `heroku-cli` to add dummy data (or do it manually).

    ```bash
    heroku run python manage.py createsuperuser
    ```
    
Here is a link to my [site].
