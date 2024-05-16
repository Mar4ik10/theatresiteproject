from django import forms

from .models import BookedSeats

class BookedSeatEdit(forms.ModelForm):
    class Meta:
        model = BookedSeats
        fields = ['name', 'seat']
        