from django.core import serializers
from django.shortcuts import HttpResponse, render

from mywatchlist.models import MyWatchlist

# Create your views here.
def mywatchlist(request):
    mywatchlist_items = MyWatchlist.objects.all()

    return render(
        request,
        'mywatchlist.html',
        {'name': 'Angga', 'mywatchlist_items': mywatchlist_items},
    )


def mywatchlist_html(request):
    mywatchlist_items = MyWatchlist.objects.all()

    return render(
        request,
        'mywatchlist.html',
        {'name': 'Angga', 'mywatchlist_items': mywatchlist_items},
    )


def mywatchlist_xml(request):
    mywatchlist_items = MyWatchlist.objects.all()

    return HttpResponse(
        serializers.serialize('xml', mywatchlist_items),
        content_type='application/xml',
    )


def mywatchlist_json(request):
    mywatchlist_items = MyWatchlist.objects.all()

    return HttpResponse(
        serializers.serialize('json', mywatchlist_items),
        content_type='application/json',
    )
