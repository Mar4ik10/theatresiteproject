from django.shortcuts import render, redirect
from . import models

# Create your views here.

def index(request):
    theatshowall = models.TheatreShow.objects.all()
    return render(request, "index.html", {"theatre": theatshowall})

def contact(request):
    return render(request, "contact.html")


def abouttheatre(request):
    return render(request, "abouttheatre.html")


def afisha(request):

    form_type = request.GET.get('form_type')
    theatshowall = models.TheatreShow.objects.all()
    scenevalues = {'mainscene': "Основна сцена", 'camscene': "Камерна сцена"}

    if form_type == 'filter_form':
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
            return redirect('/afisha/')

    elif form_type == 'search_form':
        searched = request.GET.get('search', '')
        theatreshowsbysearch = theatshowall.filter(title__icontains=searched)
        return render(request, "afisha.html", {"theatre": theatreshowsbysearch, "searched": searched})

    else:
        # Handle other cases or return the default page
        return render(request, "afisha.html", {"theatre": theatshowall})
    


def selectTickets(request, slug):
    theatshow = models.TheatreShow.objects.get(slug=slug)
    return render(request, "selectTickets.html", {
        "theatre": theatshow
    })


def placingOrder(request, slug):
    theatshow = models.TheatreShow.objects.get(slug=slug)
    a = request.GET.getlist("selected_seats[]")
    num_tickets = len(a)
    seats = []
    generalsum = 0
    for i in a:
        x = i.split('-')
        value = int(x[2])
        a = {'row':int(x[0]), 'number':int(x[1]), 'value':value}
        seats.append(a)
        generalsum += value
    
    return render(request, "placingOrder.html", {'theatre':theatshow, 'generalsum':generalsum, 'seats':seats, 'num_tickets':num_tickets})


def nextOrder(request, slug):
    theatshow = models.TheatreShow.objects.get(slug=slug)
    a = request.POST.getlist("selected_seats[]")
    print(a)
    num_tickets = len(a)
    seats = []
    generalsum = 0
    for i in a:
        x = i.split('-')
        value = int(x[2])
        a = {'row':int(x[0]), 'number':int(x[1]), 'value':value}
        seats.append(a)
        generalsum += value
    return render(request, "nextOrder.html", {'theatre':theatshow, 'generalsum':generalsum, 'seats':seats, 'num_tickets':num_tickets})


def successPay(request, slug):
    theatshow = models.TheatreShow.objects.get(slug=slug)
    a = request.POST.getlist("selected_seats[]")
    name = request.POST.get("buyer_name")
    print(name)
    print(a)
    num_tickets = len(a)
    seats = []
    generalsum = 0
    for i in a:
        x = i.split('-')
        value = int(x[2])
        a = {'row':int(x[0]), 'number':int(x[1]), 'value':value}
        seats.append(a)
        generalsum += value
    return render(request, "successPay.html", {'buyer_name':name,'theatre':theatshow, 'generalsum':generalsum, 'seats':seats, 'num_tickets':num_tickets})

def infoshow(request):
    return render(request, "infoshow.html")