from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import TheatreShowSitemap

sitemaps = {
    'theatreshows' : TheatreShowSitemap,
}

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("abouttheatre/", views.abouttheatre, name="abouttheatre"),
    path("selectTickets/<slug:slug>/", views.selectTickets, name="selectTickets"),
    path("afisha/", views.afisha, name='afisha'),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name="theatreproj/robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("placingOrder/", views.placingOrder, name="placingOrder"),
    path("nextOrder/", views.nextOrder, name="nextOrder"),
    path("successPay/", views.successPay, name="successPay"),
    path("infoshow/", views.infoshow, name="infoshow"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)