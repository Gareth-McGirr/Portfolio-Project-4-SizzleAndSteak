from django.db import models
from django.contrib.auth.models import User

# Choice fields
CAPACITY = ((2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"))
BOOKING_TIME = ((1, "12:00pm - 1:45pm"), (2, "2:00pm - 3:45pm"),
                (3, "4:00pm - 5:45pm"), (4, "6:00pm - 7:45pm"))


class Table(models.Model):
    """ Model to create Tables """
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=CAPACITY, default=2)
    wheelchair_accessible = models.BooleanField(default=True)

    class Meta:
        """ Order by table number """
        ordering = ['table_number']

    def __str__(self):
        return str(self.table_number)


class Booking(models.Model):
    """ Model to create a booking """
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_customer")
    booked_table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="booking_table")
    number_of_guests = models.IntegerField(default=2)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=BOOKING_TIME, default=1)

    class Meta:
        """ Order by booking_date and then booking_time """
        ordering = ['booking_date', 'booking_time']

    def __str__(self):
        return str(self.pk)
