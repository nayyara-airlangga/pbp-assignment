from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    catalog_items = CatalogItem.objects.all()

    context = {
        'name': 'Nayyara Airlangga Raharjo',
        'student_id': '2106652070',
        'catalog_items': catalog_items,
    }

    return render(request, 'katalog.html', context)
