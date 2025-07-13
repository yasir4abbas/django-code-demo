from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Vehicle

User = get_user_model()

class VehicleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testpass')

    def test_create_vehicle(self):
        vehicle = Vehicle.objects.create(
            user=self.user,
            make='Toyota',
            model='Camry',
            year=2020,
            plate='ABC123'
        )
        self.assertEqual(vehicle.make, 'Toyota')
        self.assertEqual(vehicle.model, 'Camry')
        self.assertEqual(vehicle.year, 2020)
        self.assertEqual(vehicle.plate, 'ABC123')

    def test_vehicle_count(self):
        vehicle1 = Vehicle.objects.create(
            user=self.user,
            make='Ford',
            model='Focus',
            year=2018,
            plate='DEF456'
        )
        vehicle2 = Vehicle.objects.create(
            user=self.user,
            make='BMW',
            model='X3',
            year=2021,
            plate='GHI789'
        )
        self.assertEqual(Vehicle.objects.count(), 2)

    def test_vehicle_has_user(self):
        vehicle = Vehicle.objects.create(
            user=self.user,
            make='Audi',
            model='A4',
            year=2022,
            plate='JKL012'
        )
        self.assertEqual(vehicle.user, self.user)
        self.assertIn(vehicle, self.user.vehicles.all())

    def test_vehicle_unique_plate(self):
        Vehicle.objects.create(
            user=self.user,
            make='Tesla',
            model='Model 3',
            year=2023,
            plate='MNO345'
        )

        with self.assertRaises(Exception):
            Vehicle.objects.create(
                user=self.user,
                make='Tesla',
                model='Model Y',
                year=2023,
                plate='MNO345'
            )

    def test_vehicle_year_validation(self):
        vehicle = Vehicle.objects.create(
            user=self.user,
            make='Ford',
            model='Mustang',
            year=2024,
            plate='PQR678'
        )
        self.assertGreaterEqual(vehicle.year, 1900)
        self.assertLessEqual(vehicle.year, 2030)
