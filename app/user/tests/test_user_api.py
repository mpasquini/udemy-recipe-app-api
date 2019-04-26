from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('user:create')
# the post req to create the user token:
TOKEN_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'prematurata',
            'name': 'pippo'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.email, payload['email'])
        self.assertTrue(user.name, payload['name'])
        self.assertTrue(user.check_password(payload['password']))
        # security check
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating a user that already exixsts"""
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'prematurata',
            'name': 'pippo'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """"Test the password must be more than 5 characters"""
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'x',
            'name': 'pippo'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'secretpass',
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_create_token_invalid_creadential(self):
        """Test that token is NOT if invalid credential is given"""
        create_user(email='pippo@askalabakara.com', password='secretpass')
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'wrong',
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """"Test that token is not created if used doesn't exists"""
        payload = {
            'email': 'pippo@askalabakara.com',
            'password': 'secretpass',
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        payload = {
            'email': 'x',
            'password': '',
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
