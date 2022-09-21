from django.shortcuts import render

from mywatchlist.models import MyWatchlist

# Create your views here.
def mywatchlist(request):
    return render(request, 'My Watchlist')


def mywatchlist_html(request):
    mywatchlist_items = MyWatchlist.objects.all()

    return render(
        request,
        'mywatchlist.html',
        {'name': 'Angga', 'mywatchlist_items': mywatchlist_items},
    )
