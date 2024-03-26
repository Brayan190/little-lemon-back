
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import Menu,Booking
from rest_framework import generics
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Queryset para todas las instancias del modelo User
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Queryset para todas las instancias del modelo User
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]