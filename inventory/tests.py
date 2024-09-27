from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class ItemTests(APITestCase):
    def setUp(self):
        self.create_url = reverse('item-list')
        self.item = Item.objects.create(
            name = 'SmartPhone',
            description = 'Electronics',
            quantity = 2,
            price = '40000.99'
        )
        self.item_url = reverse('item-detail',kwargs = {'pk' : self.item.pk})

def test_create_item(self):
    data = {'name': 'HeadPhone', 'description': 'Electronics', 'quantity': 3, 'price': '2999.99'}
    response = self.client.post(self.create_url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['name'], 'HeadPhone')
    self.assertEqual(response.data['description'], 'Electronics')
    self.assertEqual(response.data['quantity'], 3)
    self.assertEqual(response.data['price'], '2999.99')


def test_retrievee_item(self):
    response = self.client.get(self.item_url, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_CREATED)
    self.assertEqual(response.data['name'], 'SmartPhone')
    self.assertEqual(response.data['description'], 'Electronics')
    self.assertEqual(response.data['quantity'], 2)
    self.assertEqual(response.data['price'], '40000.99')


def test_update_item(self):
    updated_data = { 'name': 'UpdatedSmartPhone', 'description': 'Updated Electronics', 'quantity': 4, 'price': '45000.00' }
    response = self.client.put(self.item_url, updated_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'UpdatedSmartPhone')
    self.assertEqual(response.data['description'], 'Updated Electronics')
    self.assertEqual(response.data['quantity'], 4)
    self.assertEqual(response.data['price'], '45000.00')


def test_delete_item(self):
    response = self.client.delete(self.item_url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    response = self.client.get(self.item_url)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


