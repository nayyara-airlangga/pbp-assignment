from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
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
