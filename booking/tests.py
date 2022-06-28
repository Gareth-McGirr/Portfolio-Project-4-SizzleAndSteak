from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Booking, Table


class TestViews(TestCase):
    """
    Test cases for booking app as logged in user
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
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create Table
        table = Table.objects.create(table_number=1, capacity=2)

        # Create booking
        booking = Booking.objects.create(
            customer=self.user,
            booked_table=table,
            number_of_guests=2,
            booking_date=date.today(),
            booking_time=1
            )

    def test_booking_list(self):
        """ Test Manage Bookings """
        response = self.client.get('/booking/managebookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/managebookings.html')

    def test_booking_page(self):
        """ Test create booking when superuser """
        response = self.client.get('/booking/createbooking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/booking.html')

    def test_edit_booking_page(self):
        """ Test edit booking when owner """
        response = self.client.get('/booking/editbooking/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/edit_booking.html')

    def test_edit_unauthorized(self):
        """
        Test user cant edit another
        user booking
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'minger'
        password = 'Dirty56'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/booking/editbooking/1/')
        self.assertEqual(response.status_code, 403)

    def test_delete_unauthorized(self):
        """
        Test user cant delete another
        user booking
        """
        user_model = get_user_model()
        # Create second user for 403 errors
        username = 'minger'
        password = 'Dirty56'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/booking/delete/1/')
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """
    def test_manage_booking_auth_redirect(self):
        """ Test redirect on manage bookings """
        response = self.client.get('/booking/managebookings/')
        self.assertEqual(response.status_code, 302)

    def test_edit_booking_redirect(self):
        """ Test edit bookings """
        response = self.client.get('/booking/editbooking/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_booking_redirect(self):
        """ Test delete booking """
        response = self.client.get('/booking/delete/1/')
        self.assertEqual(response.status_code, 302)

    def test_create_booking_redirect(self):
        """ Test create booking """
        response = self.client.get('/booking/createbooking/')
        self.assertEqual(response.status_code, 302)
