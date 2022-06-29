from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to create and edit a booking
    """
    class Meta:
        """ Set fields and labels """
        model = Booking
        fields = [
            'booking_name', 'number_of_guests', 'booking_date', 'booking_time'
            ]
        booking_date = forms.DateField(help_text="Date must be a future date")
        labels = {
            'booking_name': 'Name',
            'number_of_guests': 'Number Of Guests',
            'booking_date': 'Date',
            'booking_time': 'Time',
        }

    def clean(self):
        """
        Get form data and clean, check capacity and
        throw errors when tables not available
        """
        date = self.cleaned_data['booking_date']
        time = self.cleaned_data['booking_time']
        guests = self.cleaned_data['number_of_guests']

        table_booked = None

        # Try and get object, as needed for update validation
        # pass error if on create
        try:
            table_booked = Table.objects.get(id=self.instance.booked_table.id)
        except ObjectDoesNotExist:
            pass

        # Filter tables with capacity greater or equal
        # to the number of guests
        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_time=time)
        # Get bookings on specified date
        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))
        # Iterate over tables not booked to get lowest
        # capacity table
        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.booked_table.table_number:
                    tables_with_capacity.remove(table)
                    break
        # Add booked table to list of tables
        if table_booked is not None:
            if table_booked.capacity >= guests:
                tables_with_capacity.append(table_booked)
        # Throw validation errors on form
        if date < datetime.today().date():
            raise ValidationError(
                'Invalid date - Booking cannot be in the past')
        if table_booked is not None:
            if not tables_with_capacity and table_booked.capacity < guests:
                raise ValidationError(
                    'Sorry, we do not have a table' +
                    ' available for that amount of guests'
                )
        if not tables_with_capacity:
            raise ValidationError('No tables available for this date and time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].widget.attrs['class'] = 'datepicker'
        self.fields['booking_date'].widget.attrs['autocomplete'] = 'off'
