from django.urls import path
from .views import VehicleListCreateView, VehicleDetailView

app_name = 'vehicles'

urlpatterns = [
    path('', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    path('<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
] 