from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Login Logout Test
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterTests(APITestCase):
    def test_create_account(self):
        url = reverse('register')
        data = {
            'username': 'wjddbstn023',
            'email': 'wjddbstn023@naver.com',
            'password': '1234',
            'password2': '1234',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class LoginLogoutTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="wjddbstn023", password="1234")
    
    # self에 다 담아서 한다
    def test_login(self):
        data = {
            "username": "wjddbstn023",
            "password": "1234",
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    # def test_logout(self):
    #     self.refresh = RefreshToken.for_user(self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.refresh.access_token))
    #     response = self.client.post(reverse('logout'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        