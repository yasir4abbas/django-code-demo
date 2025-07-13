from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class CustomUserModelTest(TestCase):
    def test_create_user_without_name(self):
        user = User.objects.create_user(email='test@example.com', password='testpass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email='admin@example.com', password='adminpass123')
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_email_check(self):
        user = User.objects.create_user(email='user@example.com', password='testpass')
        self.assertEqual(str(user), 'user@example.com')

    def test_user_with_names(self):
        user = User.objects.create_user(
            email='john@example.com',
            password='testpass',
            first_name='John',
            last_name='Doe'
        )
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_update_user_names(self):
        user = User.objects.create_user(email='update@example.com', password='testpass')
        user.first_name = 'Updated'
        user.last_name = 'Name'
        user.save()
        
        updated_user = User.objects.get(email='update@example.com')
        self.assertEqual(updated_user.first_name, 'Updated')
        self.assertEqual(updated_user.last_name, 'Name')
