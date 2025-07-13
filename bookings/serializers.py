from rest_framework import serializers
from .models import Booking
from vehicles.models import Vehicle
from datetime import date


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'vehicle', 'start_date', 'end_date', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'status', 'created_at', 'updated_at']


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['vehicle', 'start_date', 'end_date']

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        vehicle = attrs.get('vehicle')
        user = self.context['request'].user


        if vehicle and vehicle.user != user:
            raise serializers.ValidationError("You can only book your own vehicles")
        if start_date and start_date < date.today():
            raise serializers.ValidationError({"start_date": "Start date cannot be in the past"})
        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError({"end_date": "End date cannot be before start date"})
        return attrs 