from django.contrib import admin 
from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Register your viewsets with the router

router.register(r'booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [ 
     path('',include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('menu/', views.MenuItemsView.as_view()),
     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]