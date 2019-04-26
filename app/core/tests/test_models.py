# docker-compose run app sh -c "python manage.py test && flake8"
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_mail_successfull(self):
        """test creating a  new user and email successfull"""
        email = 'test@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_created_user_is_active(self):
        """course, lecture 30 getting redirect error
            AssertionError: 302 != 200 : Couldn't retrieve content:
            Response code was 302 (expected 200)

        checked Q&A:
        AM I got a AssertionError at test_admin.py file line 27
        --> do not resolve this case
        """
        user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='Testpass123'
        )
        self.assertTrue(user.is_active)

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='password'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password='password')
            get_user_model().objects.create_user(
                email='', password='password')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='123'
        )
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
