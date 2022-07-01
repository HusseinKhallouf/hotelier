from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class RoomType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.type


class Room(models.Model):
    AVAILABLE = "A"
    RESERVED = "R"
    ROOM_STATUS = [(AVAILABLE, "availabe"), (RESERVED, "reserved")]

    number = models.PositiveIntegerField(primary_key=True)
    status = models.CharField(max_length=1, choices=ROOM_STATUS, default=AVAILABLE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to="rooms/images")

    class Meta:
        ordering = ["number"]

    def __str__(self) -> str:
        return str(self.number)


class Reservation(models.Model):
    STATUS_PENDING = "P"
    STATUS_COMPLETE = "C"
    STATUS_FAILED = "F"
    BILL_STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_COMPLETE, "Complete"),
        (STATUS_FAILED, "Failed"),
    ]
    bill_status = models.CharField(
        max_length=1, choices=BILL_STATUS_CHOICES, default=STATUS_PENDING
    )
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, to_field="number")
