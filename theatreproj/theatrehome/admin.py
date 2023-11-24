from django.contrib import admin
from .models import TheatreShow, BookedSeats, Seat, Row

# Register your models here.

admin.site.register(TheatreShow)
admin.site.register(BookedSeats)
admin.site.register(Seat)
admin.site.register(Row)
