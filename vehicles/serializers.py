from rest_framework import serializers
from .models import Vehicle

# Added a few additional validation checks
class VehicleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'plate', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_year(self, value):
        if value < 1900 or value > 2030:
            raise serializers.ValidationError("Year must be between 1900 and 2030")
        return value

    def validate_plate(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Plate number must be at least 2 characters")
        return value.upper()

    # addign a check here that the number plate is same with other users too
    def validate(self, attrs):
        plate = attrs.get('plate', '').upper()
        instance = getattr(self, 'instance', None)
        queryset = Vehicle.objects.filter(plate=plate)
        if instance:
            queryset = queryset.exclude(pk=instance.pk)
            
        if queryset.exists():
            raise serializers.ValidationError({
                'plate': 'A vehicle with this plate number already exists.'
            })
        return attrs


# Added validation checks here as well
class VehicleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'plate']

    def validate_year(self, value):
        if value < 1900 or value > 2030:
            raise serializers.ValidationError("Year must be between 1900 and 2030")
        return value

    def validate_plate(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Plate number must be at least 2 characters")
        return value.upper()

    def validate(self, attrs):
        plate = attrs.get('plate', '').upper()
        if Vehicle.objects.filter(plate=plate).exists():
            raise serializers.ValidationError({
                'plate': 'A vehicle with this plate number already exists.'
            })
        return attrs 