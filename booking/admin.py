from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """ Class to view Tables on admin panel"""
    list_display = (
        'table_number',
        'capacity',
        'wheelchair_accessible'
    )
    list_filter = ('capacity', 'wheelchair_accessible')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Class to view bookings on admin panel """
    list_display = (
        'pk',
        'customer',
        'booked_table',
        'number_of_guests',
        'booking_date',
        'booking_time'
    )
    search_fields = ['pk', 'customer__username']
    list_filter = (
        'booking_time', 'booked_table', ('booking_date', DateRangeFilter)
    )
