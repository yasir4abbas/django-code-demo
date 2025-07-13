from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'plate', 'user', 'created_at')
    list_filter = ('make', 'year', 'created_at')
    search_fields = ('make', 'model', 'plate', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
