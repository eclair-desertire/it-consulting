from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from content.views.htmlpresent import present,service_get,privacy_policy ,all_services,all_portfolios, portfolio_get, shoq_policy
from content.views.apis import ServiceView, PortfolioView, ContactsView, RequestView

router=DefaultRouter()
router.register('services',ServiceView,basename='services')
router.register('portfolios',PortfolioView,basename='portfolio')
router.register('contacts',ContactsView,basename='contacts')
router.register('request_send',RequestView,basename='request_send')

urlpatterns = [
    path('api/',include(router.urls)),
    path('',present,name='index'),
    path('privacy_policy',privacy_policy,name='privacy_policy'),
    path('shoq_policy/',shoq_policy,name='shoq_policy'),
    path('services/',all_services,name='all_services'),
    path('services/<int:pk>/',service_get,name='service_get'),
    path('portfolios/',all_portfolios,name='all_portfolios'),
    path('portfolios/<int:pk>/',portfolio_get,name='portfolio_get'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
