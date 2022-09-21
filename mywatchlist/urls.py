from django.urls import path

from mywatchlist.views import mywatchlist_html, mywatchlist

app_name = 'mywatchlist'
urlpatterns = [
    path('', mywatchlist, name='mywatchlist'),
    path('html/', mywatchlist_html, name='mywatchlist_html'),
]
