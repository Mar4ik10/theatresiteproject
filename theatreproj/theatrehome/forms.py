from django import forms

from .models import BookedSeats

class BookedSeatForm(forms.ModelForm):
    new_seat_number = forms.IntegerField(label='New Seat Number')
    new_row_id = forms.IntegerField(label='New Row ID')

    class Meta:
        model = BookedSeats
        fields = ['name', 'show']  # Remove 'seat' and 'row'

    def clean(self):
        cleaned_data = super().clean()
        new_seat_number = cleaned_data.get('new_seat_number')
        new_row_id = cleaned_data.get('new_row_id')
        if not new_seat_number:
            self.add_error('new_seat_number', 'Seat number is required.')
        if not new_row_id:
            self.add_error('new_row_id', 'Row ID is required.')
        return cleaned_data