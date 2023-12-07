from django.shortcuts import render
from .models import Menu, BookingTable
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemsViews(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class =MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer