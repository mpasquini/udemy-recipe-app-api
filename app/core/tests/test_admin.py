from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        """create e Test client and login 1 admin and 1 user"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@here.com",
            password='123'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="test@here.com",
            password='321',
            name='test User full name'
        )
        self.client.force_login(self.user)

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
