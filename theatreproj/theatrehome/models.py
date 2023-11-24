from django.db import models

# Create your models here.

class TheatreShow(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="theatreimages/")
    genre = models.CharField(max_length=100)
    num_scene = models.IntegerField()
    date = models.DateTimeField()
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
    

class Row(models.Model):
    price = models.IntegerField()

class Seat(models.Model):
    seat_no = models.IntegerField()
    row = models.ForeignKey(Row, on_delete=models.CASCADE)


class BookedSeats(models.Model):
    show = models.ForeignKey(TheatreShow, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)