from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('menu', views.MenuItemsViews.as_view(), name = 'menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name = 'single-menu'),
    path('booking', views.BookingViewSet.as_view({'get': 'list'}), name='booking')
]