from django.core import serializers
from django.shortcuts import HttpResponse, render

from mywatchlist.models import MyWatchlist

# Create your views here.
def mywatchlist(request):
    mywatchlist_items = MyWatchlist.objects.all()

    # Bonus
    watch_status = ""
    watched_count = MyWatchlist.objects.filter(watched=True).count()

    if mywatchlist_items.count() - watched_count < watched_count:
        watch_status = "Selamat, kamu sudah banyak menonton!"
    else:
        watch_status = "Wah, kamu masih sedikit menonton!"

    return render(
        request,
        'mywatchlist.html',
        {
            'name': 'Angga',
            'watch_status': watch_status,
            'mywatchlist_items': mywatchlist_items,
        },
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
