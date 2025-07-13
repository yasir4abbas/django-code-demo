from django.test import TestCase
from django.contrib.auth import get_user_model
from vehicles.models import Vehicle
from .models import Booking
from datetime import date, timedelta

User = get_user_model()

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')
        self.vehicle = Vehicle.objects.create(
            user=self.user,
            make='Toyota',
            model='Camry',
            year=2020,
            plate='ABC123'
        )

    def test_create_booking(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=3)
        booking = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date,
            end_date=end_date,
            status='pending'
        )
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.vehicle, self.vehicle)
        self.assertEqual(booking.status, 'pending')

    def test_booking_default_status(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=2)
        booking = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date,
            end_date=end_date
        )
        self.assertEqual(booking.status, 'pending')

    def test_booking_count(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=1)
        
        booking1 = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date,
            end_date=end_date
        )
        booking2 = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date + timedelta(days=1),
            end_date=end_date + timedelta(days=1)
        )
        self.assertEqual(Booking.objects.count(), 2)

    def test_booking_dates_validation(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=3)
        booking = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date,
            end_date=end_date
        )
        self.assertGreater(booking.end_date, booking.start_date)

    def test_booking_user_relationship(self):
        start_date = date.today()
        end_date = start_date + timedelta(days=2)
        booking = Booking.objects.create(
            user=self.user,
            vehicle=self.vehicle,
            start_date=start_date,
            end_date=end_date
        )
        self.assertEqual(booking.user, self.user)
        self.assertIn(booking, self.user.bookings.all())
