from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Menu, MenuItem


class TestViews(TestCase):
    """
    Test cases for menu app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = "gareth"
        password = "£123Hatfdn"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_create_menu_page(self):
        """ Test create menu """
        response = self.client.get('/menu/createmenu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/create_menu.html')


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """
    def test_create_menu_auth_redirect(self):
        """ Test redirect on create menu """
        response = self.client.get('/menu/createmenu/')
        self.assertEqual(response.status_code, 302)

    def test_edit_menu_redirect(self):
        """ Test edit menu """
        response = self.client.get('/menu/editmenu/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_menu_redirect(self):
        """ Test delete menu """
        response = self.client.get('/menu/delete/1/')
        self.assertEqual(response.status_code, 302)

    def test_manage_menu_redirect(self):
        """ Test manage menu """
        response = self.client.get('/menu/managemenus/')
        self.assertEqual(response.status_code, 302)


class TestUnsecuredViews(TestCase):
    """ Test views no auth required """
    def test_menu_view(self):
        """ Test view menu """
        response = self.client.get('/menu/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menus.html')
