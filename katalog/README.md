# Assignment 2: Introduction to Django and Models View Template (MVT) Concept

[Heroku Site]: https://pbp-web-assignment.herokuapp.com
[site]: https://pbp-web-assignment.herokuapp.com
[PBP assignments]: https://github.com/pbp-fasilkom-ui/assignment-repository

[MVT Diagram]: /static/Django-MVT-Architecture.jpg

Link to Site: [Heroku Site]

## Django MVT Architecture Request-Response Diagram

Below is a diagram of a request and response handled via Django's MVT architecture.

![MVT Diagram]

A client sends a request to the Django server. This request will be handled by the appropriate route based on the request url (`urls.py`). The view function assigned to the route will handle the request. The view normally contains the business logic to be done (`views.py`). Should a view need to mutate or query data from a database, the appropriate model will be used to interface with the database (`models.py`). The view then renders an HTML document. This HTML document is rendered from a template. This template will be filled with data from a context of the view for every corresponding request (`templates/*.html`). The rendered HTML is then returned from the view as a web page in the form of a response, with the HTML as its response body to the client.

## Why use virtual environments? Can we create a Django project without it?

The answer is we can. However, it is not advised. The reason is that it might conflict with other project's requirements/dependencies. Say we have a Django project that uses version A of MYPY. Another project might require a different version of MYPY. To avoid conflicting versions and potentially breaking projects, we can use virtual environments to isolate a project's dependencies from one another. It also effectively means making the project independent of the host operating systems' Python packages since a virtual environment has its own packages.

## Implementing points 1-4

This guide assumes that a katalog is made from the latest version of the template repository for [PBP assignments] as of Assignment 2.

1. Create a `show_catalog` function in `katalog.views`

```python
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    catalog_items = CatalogItem.objects.all()

    context = {
        'name': 'Your Full Name',
        'student_id': 'Your Student ID number',
        'catalog_items': catalog_items,
    }

    return render(request, 'katalog.html', context)
```

`CatalogItem` is a Django model used to retrieve data about catalog items in the database. A context object is created which stores our name, student id number, and the retrieved catalog items via the `CatalogItem` model. We then render the `katalog.html` template with the created context to fill the template. 

2. Create `app_name` and `urlpatterns` list with contains the routes for the katalog app inside of `katalog.urls`.

```python
from django.urls import path
from katalog.views import show_catalog

app_name = "katalog"
urlpatterns = [path('', show_catalog, name='show_catalog')]
```

The path is `''` which means it will be the `/` route of certain route. It will be further explained in the next step. It is assigned the `show_catalog` function from `katalog.views` which means that function will handle the request to this route. 

3. Include the `urlpatterns` from `katalog.urls` in `project_django.urls`.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```

The `katalog/` is mapped to the `urlpatterns` from `katalog.urls`. This means that every route in `katalog.urls` will be prefixed by `katalog`. Which means our previous `''` route will be assigned the full path of `<hostname>/katalog/`. 

4. Modify the `katalog.html` template and map the appropriate context properties to its blocks.

```html
{% extends 'base.html' %}

 {% block content %}

  <h1>Lab 1 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{ name }}</p>

  <h5>Student ID: </h5>
  <p>{{ student_id }}</p>

  <table>
    <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for item in catalog_items %}
    <tr>
      <td>{{ item.item_name }}</td>
      <td>{{ item.item_price }}</td>
      <td>{{ item.item_stock }}</td>
      <td>{{ item.rating }}</td>
      <td>{{ item.description }}</td>
      <td>{{ item.item_url }}</td>
    </tr>
    {% endfor %}
  </table>

 {% endblock content %}
```

The template will require a name, a student id number, and a list of catalog items. This will be provided by `katalog.views`'s' `show_catalog` function's context upon rendering.

5. Deploying to Heroku

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

Here is a link to my [site].
