from django.db import models
from django.template.defaultfilters import slugify
import datetime
from django.urls import reverse

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
    date = models.DateField()
    time = models.TimeField(default=datetime.time(18, 00))
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    formatted_date = models.CharField(max_length=255, blank=True, null=True)
    formatted_time = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('selectTickets', kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        self.formatted_date = self.date.strftime("%a, %d / %m / %Y")
        self.formatted_time = self.time.strftime("%H:%M")

        if not self.slug:
            self.slug = slugify(self.title)

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
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    
    name_card = models.CharField(max_length=255)
    