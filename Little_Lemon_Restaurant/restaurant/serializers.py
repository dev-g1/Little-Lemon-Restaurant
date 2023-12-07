from rest_framework import serializers
from .models import Menu, BookingTable

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory']



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'