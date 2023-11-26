from django.contrib.sitemaps import Sitemap
from . import models

class TheatreShowSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9


    def items(self):
        return models.TheatreShow.objects.all()
    

    def lastmod(self, obj):
        return obj.created