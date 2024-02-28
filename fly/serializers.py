from rest_framework import serializers

from fly.models import FlightRoutes


class FlightRoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightRoutes
        fields = '__all__'
