from django.contrib import admin
from .models import Table, Booking
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'table_number',
        'capacity',
        'wheelchair_accessible'
    )
    list_filter = ('capacity', 'wheelchair_accessible')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'customer',
        'booked_table',
        'number_of_guests',
        'booking_date',
        'booking_time'
    )
    search_fields = ['pk', 'customer__username']
    list_filter = ('booking_time', 'booked_table', ('booking_date', DateRangeFilter))
