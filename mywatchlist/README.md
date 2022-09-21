# Assignment 3: Implement Data Delivery using Django

[Link to Site]: https://pbp-web-assignment.herokuapp.com
[site]: https://pbp-web-assignment.herokuapp.com
[Assignment 2]: https://github.com/nayyara-airlangga/pbp-assignment/tree/acf171b7d281704d1d98683fba9dea594b8c35bf

[PostmanHTML]: /static/MyWatchlist-HTML.png
[PostmanXML]: /static/MyWatchlist-XML.png
[PostmanJSON]: /static/MyWatchlist-JSON.png

[Link to Site]

## What are the differences between JSON, XML, and HTML?

Let's focus on HTML and XML first. Both are known as markup languages. Markup languages has a set of symbols and elements which are inserted in text to structure and format text according to a standard.
HTML stands for Hypertext Markup Language while XML stands for Extensible Markup Language. Both HTML and XML use tags to wrap content in order to give structure, hierarchy,
and better readability. However, HTML was designed to better fit the purpose of showing data in the form of web pages while XML was made with the intention to serve as a
format for data storage and transfer. Therefore, XML is almost never used to be served in a web page where the client could see directly but rather as data being delivered
to be used. JSON is also a form of way to structure data for transport and storage. It stands for JavaScript Object Notation. However, due to its easy readability and
how popular the usage of JavaScript in various client and server side applications, JSON is more commonly used. JSON is annotated in the form of keys and values, similar to maps
or dictionaries, adding more compatibility with other languages outside of JavaScript, further increasing its flexibility.

## Why do we need data delivery in a platform implementations?

Almost all platforms/applications will read, modify, and send data in some way. This is why we need a data delivery standard so that it is easy to build platforms that
can integrate and share its data when needed.

## Implementing this assignment's checklists

The steps taken here assumes that we are using the latest version of my PBP Assignment repository for [Assignment 2]. The steps written here also doesn't include
steps to implement the bonus. Although I did implement the bonus, I think it's better to just explain during the demonstration.

1. Create the `mywatchlist` app if we haven't already.

    ```bash
    python manage.py startapp mywatchlist
    ```
    
2. Add `mywatchlist` to `INSTALLED_APPS` in `project_django/settings.py`.

    ```python
    INSTALLED_APPS = [
        # ...
        'mywatchlist',
    ]
    ```
    
3. Create the `MyWatchlist` model.

    ```python
    from django.core.validators import MaxValueValidator, MinValueValidator
    from django.db import models


    class MyWatchlist(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length=255)
        rating = models.FloatField(
            validators=[MaxValueValidator(5.0), MinValueValidator(0.0)]
        )
        release_date = models.DateField()
        review = models.TextField()
    ```
  
    Once the model is created, run `python manage.py makemigrations` to make migrations for the new model and `python manage.py migrate` to apply the migrations to the
    database.
  
4. Create a JSON file that acts as a seed for 10 `MyWatchlist` objects in `mywatchlist/fixtures/initial_mywatchlist_data.json`.

    ```json
    [
      {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
          "watched": true,
          "title": "The Avengers",
          "rating": 3,
          "release_date": "2012-05-04",
          "review": "The comedic timing, coupled with his ability to maintain the authenticity of the characters, is worthy of praise. The Avengers delivers a popcorn feast that's the perfect summer kickoff."
        } 
      },
      // ...
    ]
    ```
    
    Run `python manage.py loaddata initial_mywatclist_data.json` to load the `MyWatchlist` objects to the database.
    
5. Create `mywatchlist_html`, `mywatchlist_xml`, `mywatchlist_json` view function in `mywatchlist/views.py`.

    ```python
    from django.core import serializers
    from django.shortcuts import HttpResponse, render

    from mywatchlist.models import MyWatchlist
    ```
    
    The `MyWatchlist` model will be used to get the data from the database to be displayed by the view functions.
    
    ```python
    def mywatchlist_html(request):
        mywatchlist_items = MyWatchlist.objects.all()

        return render(
            request,
            'mywatchlist.html',
            {'name': 'Angga', 'mywatchlist_items': mywatchlist_items},
        )
    ```
    
    `mywatchlist_html` renders an HTML document from the `mywatchlist.html` (created later) template which will be given the name and watchlist items arguments.
    The watchlist items is from the `MyWatchlist` model.
    
    ```python
    def mywatchlist_xml(request):
        mywatchlist_items = MyWatchlist.objects.all()

        return HttpResponse(
            serializers.serialize('xml', mywatchlist_items),
            content_type='application/xml',
        )
    ```
    
    `mywatchlist_xml` renders the watchlist items in XML format.
    
    ```python
        def mywatchlist_json(request):
        mywatchlist_items = MyWatchlist.objects.all()

        return HttpResponse(
            serializers.serialize('json', mywatchlist_items),
            content_type='application/json',
        )
    ```
    
    `mywatchlist_json` renders the watchlist items in JSON format.
    
6. Add a `mywatchlist/` path in the `urlpatterns` of `project_django/urls.py`. It will add a `/mywatchlist` route from the base path.

   ```python
   urlpatterns = [
       # ...
       path('mywatchlist/', include('mywatchlist.urls')),
   ]
   ```
7. Create a `urls.py` in `mywatchlist` and add the `app_name` and `urlpatterns` and add the respective handlers according to the path name and data delivery method.

    ```python
    from django.urls import path

    from mywatchlist.views import (
        mywatchlist_html,
        mywatchlist,
        mywatchlist_json,
        mywatchlist_xml,
    )

    app_name = 'mywatchlist'
    urlpatterns = [
        path('html/', mywatchlist_html, name='mywatchlist_html'),
        path('xml/', mywatchlist_xml, name='mywatchlist_xml'),
        path('json/', mywatchlist_json, name='mywatchlist_json'),
    ]
    ```
    
    This'll add `/mywatchlist/html`, `/mywatchlist/xml`, and `/mywatchlist/html` to the routes/urls with the appropriate view functions assigned according to the data delivery
    method (HTML, XML, or JSON).
    
8. Create `mywatchlist.html` in `mywatchlist/templates` which will be used as the HTML template rendered by the `mywatchlist_html` function.

    ```html
    {% extends 'base.html' %}

    {% block content %}

    <h1>{{ name }}'s Watchlist</h1>

    {% if watch_status %}
    <h3>{{ watch_status }}</h3>
    {% endif %}

    <table>
      <tr style='font-size: 18px'>
        <th>Title</th>
        <th>Rating</th>
        <th>Release Date (Theaters)</th>
        <th>Watched</th>
        <th>Review</th>
      </tr>
      {% for item in mywatchlist_items %}
      <tr>
        <td>{{ item.title }}</td>
        <td>{{ item.rating }}</td>
        <td>{{ item.release_date }}</td>
        <td>{{ item.watched }}</td>
        <td>{{ item.review }}</td>
      </tr>
      {% endfor %}
    </table>

    {% endblock content %}
    ```
    
9. Create unit tests in `mywatchlist/tests.py`.

    ```python
    from django.test import Client, TestCase
    from django.urls import reverse

    class MyWatchlistTestcase(TestCase):
        def setUp(self):
            self.__client = Client()

        def test_html_view_ok(self):
            url = reverse('mywatchlist:mywatchlist_html')
            res = self.__client.get(url)

            self.assertEqual(res.status_code, 200)

        def test_xml_view_ok(self):
            url = reverse('mywatchlist:mywatchlist_xml')
            res = self.__client.get(url)

            self.assertEqual(res.status_code, 200)

        def test_json_view_ok(self):
            url = reverse('mywatchlist:mywatchlist_json')
            res = self.__client.get(url)

            self.assertEqual(res.status_code, 200)
    ```
    
    To run the tests, run `python manage.py test`.
    
10. Modify the `release` block of the `Procfile`.

    ```
    release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_mywatchlist_data.json'
    ```
    
    This is done to make sure that Heroku loads the fixture data from `initial_mywatchlist_data.json`.
    
11. Deploy the site to Heroku.

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

## Postman Screenshots

### HTML Route
![PostmanHTML]

### XML Route
![PostmanXML]

### JSON Route
![PostmanJSON]
