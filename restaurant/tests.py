from django.test import TestCase
from .models import Menu
# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item_result = item.get_item()
        self.assertEqual(item_result, "IceCream : 80")
