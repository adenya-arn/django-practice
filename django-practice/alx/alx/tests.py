from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('user-list')
        self.User = User.objects.create_user(username='test user', email='test@gmail.com')
    
    def test_user_list(self):
        response =self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


        usernames = [user['username'] for user in response.data]
        self.assertIn('test user', usernames)  
        self.assertTrue(len(usernames) != 0)


