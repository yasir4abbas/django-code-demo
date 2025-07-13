from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Booking
from .serializers import BookingSerializer, BookingCreateSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        bookings = Booking.objects.filter(user=self.request.user)
        start = self.request.query_params.get('from')

        if start:
            try:
                start_date = datetime.strptime(start, '%Y-%m-%d').date()
                bookings = bookings.filter(start_date__gte=start_date)
            except ValueError:
                pass

        end = self.request.query_params.get('to')
        if end:
            try:
                end_date = datetime.strptime(end, '%Y-%m-%d').date()
                bookings = bookings.filter(end_date__lte=end_date)
            except ValueError:
                pass

        return bookings

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        return BookingSerializer
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
