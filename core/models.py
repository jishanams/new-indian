from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=50)
    service_type = models.CharField(max_length=100)
    preferred_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_model} ({self.preferred_date})"
