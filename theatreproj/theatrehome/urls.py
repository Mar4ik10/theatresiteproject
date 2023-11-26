from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("abouttheatre/", views.abouttheatre, name="abouttheatre"),
    path("selectTickets/<slug:show_id>/", views.selectTickets, name="selectTickets"),
    path("afisha/", views.afisha, name='afisha'),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="theatreproj/robots.txt", content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)