from django.urls import path

from mywatchlist.views import (
    mywatchlist_html,
    mywatchlist,
    mywatchlist_json,
    mywatchlist_xml,
)

app_name = 'mywatchlist'
urlpatterns = [
    path('', mywatchlist, name='mywatchlist'),
    path('html/', mywatchlist_html, name='mywatchlist_html'),
    path('xml/', mywatchlist_xml, name='mywatchlist_xml'),
    path('json/', mywatchlist_json, name='mywatchlist_json'),
]
