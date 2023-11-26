from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    theatshowall = models.TheatreShow.objects.all()
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def abouttheatre(request):
    return render(request, "abouttheatre.html")

def placingOrder(request):
    return render(request, "placingOrder.html")

def selectTickets(request, show_id):
    theatshow = models.TheatreShow.objects.get(pk=show_id)
    
    return render(request, "selectTickets.html", {
        "theatre": theatshow
    })

def afisha(request):
    theatshowall = models.TheatreShow.objects.all()
    scenevalues = {'mainscene': "Основна сцена", 'camscene': "Камерна сцена"}
        
    if request.method =="GET":
        date_filter = request.GET.get('input-date', None)
        typeofscene = request.GET.get('input-select', None)
        if date_filter:
            theatreshows = theatshowall.filter(date=date_filter)
            return render(request, "afisha.html", {"theatre": theatreshows})
        
        if typeofscene:
            for i, j in scenevalues.items():
                if typeofscene == i:
                    theatreshows = theatshowall.filter(typescene=j)
                    return render(request, "afisha.html", {"theatre": theatreshows})
        
    return render(request, "afisha.html", {"theatre": theatshowall})