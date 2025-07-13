from django.urls import path
from .views import BookingListCreateView

app_name = 'bookings'

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),
] 