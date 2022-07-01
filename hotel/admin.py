from argparse import Action
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
from .models import Reservation, Room, RoomType
from datetime import date

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = ["set_available"]
    list_display = ["number", "status", "room_type", "reservations_count"]
    list_editable = ["status"]
    list_select_related = ["room_type"]
    list_filter = ["status", "room_type"]
    list_per_page = 10
    search_fields = ["number"]  # __startwith, ... lookup types
    autocomplete_fields = ["room_type"]

    @admin.display()
    def reservations_count(self, room: Room):

        url = (
            reverse(
                "admin:hotel_reservation_changelist"  # reverse view name to url by the following structure admin:app_model_page
            )
            + "?"
            + urlencode({"room__number": str(room.number)})
        )

        return format_html('<a href="{}"">{}</a>', url, room.reservations_count)

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(reservations_count=Count("reservation"))
        )

    @admin.action(description="Set available")
    def set_available(self, request, queryset):
        count = queryset.update(status="A")
        self.message_user(request, f"{count} Rooms set to available")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "room", "reservation_status"]

    @admin.display()
    def reservation_status(self, reservation: Reservation):
        if reservation.date.date() >= date.today():
            return "upcoming"
        return "past"


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    search_fields = ["type"]
