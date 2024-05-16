from django import forms

from .models import BookedSeats

class BookedSeatForm(forms.ModelForm):
    class Meta:
        model = BookedSeats
        fields = ['seat']
        