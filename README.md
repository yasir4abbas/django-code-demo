# OneNow

A Django REST API for vehicle booking management.

## Quick Start Guide by me

1. **Clone and install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

3. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

4. **Start the server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Admin**: http://localhost:8000/admin/
- **Docs**: http://localhost:8000/swagger/

## Features

- User authentication with JWT
- Vehicle management
- Booking system
- RESTful APIs with Swagger documentation

## Testing

Run tests with:
```bash
python manage.py test
``` 

## Sample API Requests

The API uses email-based authentication with JWT tokens, this is presisly why all auth is added to remove the need for username authentication. All requests (except registration and login) require an `Authorization` header with the Bearer token.

### Authentication

#### Register User
```http
POST /api/register/
Content-Type: application/json

{
    "email": "demo@test.com",
    "password": "testpass1",
    "password2": "testpass1",
    "first_name": "John",
    "last_name": "Doe"
}
```

**Response:**
```json
{
    "email": "demo@test.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### Login User
```http
POST /api/login/
Content-Type: application/json

{
    "email": "demo@test.com",
    "password": "testpass1"
}
```

**Response:**
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MjUxMjQ5MSwiaWF0IjoxNzUyNDI2MDkxLCJqdGkiOiI2OTYyYjM1NzJkYWI0M2FhODY1ZWJlNDE3NGFjY2IwNCIsInVzZXJfaWQiOjF9.zschheLFYtCUD6FrhU3D5dNSQ3FTtidft4tEfmhem2c",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyNDI5NjkxLCJpYXQiOjE3NTI0MjYwOTEsImp0aSI6IjI1NzdhMThlZDUzMTQ3YzNhNTVhZjg1ZGZjZDQ0N2Q5IiwidXNlcl9pZCI6MX0.vLZPl9NfCl_EPMbH9btX7QecuFor7HtZKtlwmZB9FnY",
    "email": "demo@test.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

### Vehicle Management

#### List All Vehicles
```http
GET /api/vehicles/
Authorization: Bearer {access_token}
```

**Response:**
```json
[
    {
        "id": 2,
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "plate": "ABC123",
        "user": "demo@test.com",
        "created_at": "2025-07-13T14:43:18.101158Z",
        "updated_at": "2025-07-13T14:43:18.101200Z"
    }
]
```

#### Create Vehicle
```http
POST /api/vehicles/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "make": "Honda",
    "model": "Civic",
    "year": 2021,
    "plate": "XYZ789"
}
```

#### Get Vehicle Details
```http
GET /api/vehicles/{vehicle_id}/
Authorization: Bearer {access_token}
```

### Booking Management

#### List All Bookings
```http
GET /api/bookings/
Authorization: Bearer {access_token}
```

**Response:**
```json
[
    {
        "id": 2,
        "user": "demo@test.com",
        "vehicle": 2,
        "start_date": "2025-08-01",
        "end_date": "2025-08-07",
        "status": "pending",
        "created_at": "2025-07-13T16:46:02.609940Z",
        "updated_at": "2025-07-13T16:46:02.609994Z"
    }
]
```

#### Create Booking
```http
POST /api/bookings/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "vehicle": 2,
    "start_date": "2025-08-01",
    "end_date": "2025-08-07"
}
```

#### Get Booking Details
```http
GET /api/bookings/{booking_id}/
Authorization: Bearer {access_token}
```

### Error Responses

#### Authentication Error (401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

#### Permission Error (403)
```json
{
    "detail": "You do not have permission to perform this action."
}
```

#### Not Found Error (404)
```json
{
    "detail": "Not found."
}
```

#### Validation Error (400)
```json
{
    "field_name": [
        "This field is required."
    ]
}
```

## About 1Now

1Now helps vehicle owners to bypass third-party platforms like Turo and build their own rental ecosystem, giving full control of the booking experience and they don't take the full charge it seems.

---

**PLUG!** [Visit my other Work!](https://yasirabbas.tech)

