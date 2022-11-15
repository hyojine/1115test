from django.urls import reverse
from rest_framework.test import APITestCase

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse('userview')
        user_data = {
            "username":"test",
            "fullname":"테스터",
            "email":"test@testuser.com",
            "password":"password",
        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.data['message'],"가입 완료!!")