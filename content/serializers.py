from rest_framework import serializers
from content.models import Portfolio, Contacts, Service, OurClients, MainPageDigits, Testimonal
from bot.models import Request

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Portfolio
        fields='__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields='__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields='__all__'

class OurClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurClients
        fields='__all__'

class MainPageDigitsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MainPageDigits
        fields='__all__'

class TestimonalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Testimonal
        fields='__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields='__all__'
        