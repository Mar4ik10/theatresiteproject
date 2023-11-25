from django.db import models
from django.utils import timezone

# Create your models here.

class TheatreShow(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="public/theatreimages")
    genre = models.CharField(max_length=100)

    SCENES_CHOICES = [
        ("Основна сцена", "Основна сцена"),
        ("Камерна сцена", "Камерна сцена")
    ]

    typescene = models.CharField(max_length=150, choices=SCENES_CHOICES, default="Основна сцена")
    num_scene = models.IntegerField()
    date = models.DateTimeField()
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    formatted_date = models.CharField(max_length=255, blank=True, null=True)
    formatted_time = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.formatted_date = self.date.strftime("%a, %d / %m / %Y")
        self.formatted_time = self.date.strftime("%H:%M")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.formatted_date}"
    

class Row(models.Model):
    price = models.IntegerField()

class Seat(models.Model):
    seat_no = models.IntegerField()
    row = models.ForeignKey(Row, on_delete=models.CASCADE)


class BookedSeats(models.Model):
    show = models.ForeignKey(TheatreShow, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)