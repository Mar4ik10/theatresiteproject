from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("abouttheatre/", views.abouttheatre, name="abouttheatre"),
    path("selectTickets/<int:show_id>/", views.selectTickets, name="selectTickets"),
    path("afisha/", views.afisha, name='afisha'),
    path("placingOrder/", views.placingOrder, name="placingOrder"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)