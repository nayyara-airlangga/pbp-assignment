from django.test import TestCase
from django.urls import resolve, reverse

from katalog.models import CatalogItem
from katalog.views import show_catalog

# Create your tests here.
class KatalogTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(
            item_name='Bread',
            item_price=8000,
            item_stock=10,
            description='Fresh wheat bread',
            rating=4,
            item_url='http://localhost:65535',
        )
        CatalogItem.objects.create(
            item_name='Milk',
            item_price=4000,
            item_stock=12,
            description='Fresh milk',
            rating=5,
            item_url='http://localhost:65534',
        )

    def test_amount_of_catalog_items(self):
        amount_of_catalog_items = CatalogItem.objects.count()

        self.assertEqual(2, amount_of_catalog_items)

    def test_get_catalog_items_by_item_name(self):
        bread = CatalogItem.objects.get(item_name='Bread')

        self.assertEqual(bread.item_name, 'Bread')
        self.assertEqual(bread.description, 'Fresh wheat bread')

    def test_katalog_url_correct_view_function(self):
        # reverse can be used to get the url from a pattern

        katalog_url_view_function = resolve(reverse('katalog:show_catalog')).func

        self.assertEqual(katalog_url_view_function, show_catalog)
