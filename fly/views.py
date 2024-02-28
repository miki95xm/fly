from rest_framework import permissions, viewsets

from fly.models import FlightRoutes
from fly.serializers import FlightRoutesSerializer


class FlightRoutesViewSet(viewsets.ModelViewSet):
    queryset = FlightRoutes.objects.all()
    serializer_class = FlightRoutesSerializer
    permission_classes = [permissions.AllowAny]
