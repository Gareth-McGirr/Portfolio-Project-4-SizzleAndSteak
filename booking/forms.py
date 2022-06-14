from datetime import datetime
from django.core.exceptions import ValidationError
from django import forms
from .models import Booking, Table


class BookingForm(forms.ModelForm):
    """
    Form to create and edit a booking

    Args:
        forms (_type_): _description_

    Raises:
        ValidationError: _description_
        ValidationError: _description_
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
        
        if date < datetime.today().date():
            raise ValidationError('Invalid date - Booking cannot be in the past')
        if not tables_with_capacity:
            raise ValidationError('No tables available for this date and time')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date'].widget.attrs['class'] = 'datepicker'
        self.fields['booking_date'].widget.attrs['autocomplete'] = 'off'
