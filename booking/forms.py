from datetime import datetime
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to create and edit a booking
    """
    class Meta:
        model = Booking
        fields = ['number_of_guests',
                'booking_date', 'booking_time']
        booking_date = forms.DateField(help_text="Date must be a future date")
        labels = {
            'number_of_guests': 'Number Of Guests',
            'booking_date': 'Date',
            'booking_time': 'Time',
        }

    def clean(self):
        date = self.cleaned_data['booking_date']
        time = self.cleaned_data['booking_time']
        guests = self.cleaned_data['number_of_guests']

        table_booked = None

        try:
            table_booked = Table.objects.get(id=self.instance.booked_table.id)
        except ObjectDoesNotExist:
            pass

        bookings_on_requested_date = Booking.objects.filter(
            booking_date=date, booking_time=time)

        tables_with_capacity = list(Table.objects.filter(
            capacity__gte=guests
        ))

        for booking in bookings_on_requested_date:
            for table in tables_with_capacity:
                if table.table_number == booking.booked_table.table_number:
                    tables_with_capacity.remove(table)
                    break

        if table_booked is not None:
            if table_booked.capacity >= guests:
                tables_with_capacity.append(table_booked)

        if date < datetime.today().date():
            raise ValidationError(
                'Invalid date - Booking cannot be in the past')
        if table_booked is not None:
            if not tables_with_capacity and table_booked.capacity < guests:
                raise ValidationError(
                    'Sorry, we do not have a table available for that amount of guests')
        if not tables_with_capacity:
            raise ValidationError('No tables available for this date and time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].widget.attrs['class'] = 'datepicker'
        self.fields['booking_date'].widget.attrs['autocomplete'] = 'off'