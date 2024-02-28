from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=255)


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=255)
    airline = models.ForeignKey("Airline")
    fuel_tank = models.FloatField()
    fuel_consumption = models.FloatField(help_text="Liters per hour")
    max_distance = models.IntegerField()


class FlightRoutes(models.Model):
    fuel_consumption = models.FloatField()
    start_point = models.CharField(max_length=8)
    end_point = models.CharField(max_length=8)
    flight_time = models.TimeField()

