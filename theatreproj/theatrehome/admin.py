from django.contrib import admin
from .models import TheatreShow, BookedSeats, Seat, Row

# Register your models here.

class TheatreShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(TheatreShow, TheatreShowAdmin)
admin.site.register(BookedSeats)
admin.site.register(Seat)
admin.site.register(Row)
