from django.contrib.sitemaps import Sitemap

from content.models import Service

class ServiceSitemap(Sitemap):
		changefreq = "weekly"
		priority = 0.9
		
		def items(self):
				return Service.objects.all()
		
		def lastmod(self, obj):
				return obj.publish