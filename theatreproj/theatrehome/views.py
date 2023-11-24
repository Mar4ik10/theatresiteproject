from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def abouttheatre(request):
    return render(request, "abouttheatre.html")

def selectTickets(request, show_id):
    theatshow = models.TheatreShow.objects.get(pk=show_id)
    
    return render(request, "selectTickets.html", {
        "theatre": theatshow
    })