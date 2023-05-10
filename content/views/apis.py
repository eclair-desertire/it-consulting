from rest_framework.viewsets import mixins, GenericViewSet, ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from bot.tgbot import send_request_from_django
from bot.models import Request
from content.models import Portfolio, Contacts, Service, OurClients, MainPageDigits, Testimonal
from content.serializers import ServiceSerializer, PortfolioSerializer, ContactsSerializer, RequestSerializer
import logging


logger=logging.getLogger(__name__)


class ServiceView(GenericViewSet,mixins.ListModelMixin):
    serializer_class=ServiceSerializer
    queryset=Service.objects.all()

    def list(self, request, *args, **kwargs):
        logger.warning(request.headers)
        try:
            if request.headers['bot-request-token']==settings.BOT_REQUEST_TOKEN:
                return super().list(request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        

class PortfolioView(GenericViewSet,mixins.ListModelMixin):
    serializer_class=PortfolioSerializer
    queryset=Portfolio.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            if request.headers['bot-request-token']==settings.BOT_REQUEST_TOKEN:
                return super().list(request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
class ContactsView(GenericViewSet,mixins.ListModelMixin):
    serializer_class=ContactsSerializer
    queryset=Contacts.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            if request.headers['bot-request-token']==settings.BOT_REQUEST_TOKEN:
                return super().list(request, *args, **kwargs)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
class RequestView(GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RequestSerializer
    queryset=Request.objects.all()

    def create(self, request, *args, **kwargs):
        super().create(request,*args,**kwargs)
        send_request_from_django(request.data)
        return Response(data={'success':True},status=status.HTTP_200_OK)