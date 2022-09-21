from django.shortcuts import render

# Create your views here.
def show_mywatchlist(request):
    return render(request, 'My Watchlist')
