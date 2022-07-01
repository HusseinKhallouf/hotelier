from django.urls import include, path

from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("rooms", views.RoomViewSet, basename="rooms")

room_router = routers.NestedDefaultRouter(router, "rooms", lookup="room")
room_router.register(
    "reservations", views.ReservationViewSet, basename="room-reservation"
)


urlpatterns = [
    path("reservations/", views.ReservationsList.as_view()),
    path("", include(router.urls)),
    path("", include(room_router.urls)),
]
