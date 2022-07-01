from rest_framework import serializers

from .models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["number", "room_type", "status", "image"]


class ReservationSerializer(serializers.ModelSerializer):
    room_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Reservation
        fields = ["id", "bill_status", "date", "user", "room_id"]

    def create(self, validated_data):
        room_id = self.context["room_id"]
        return Reservation.objects.create(room_id=room_id, **validated_data)
