from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleCreateSerializer


class VehicleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        """Return only vehicles belonging to the authenticated user"""
        return Vehicle.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """Use different serializer for create vs list"""
        if self.request.method == 'POST':
            return VehicleCreateSerializer
        return VehicleSerializer

    def perform_create(self, serializer):
        """Automatically assign the current user to the vehicle"""
        serializer.save(user=self.request.user)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer

    def get_queryset(self):
        """Return only vehicles belonging to the authenticated user"""
        return Vehicle.objects.filter(user=self.request.user)
