from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPagination
from .models import Reservation, Room, RoomType
from .serializers import ReservationSerializer, RoomSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields =['room_type_id','status']
    search_fields =['room_type__type']
    pagination_class = CustomPagination


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(room_id=self.kwargs["room_pk"])

    def get_serializer_context(self):
        return {"room_id": self.kwargs["room_pk"]}


class ReservationsList(APIView):
    def get(self, request):
        queryset = Reservation.objects.all()
        serializer = ReservationSerializer(queryset, many=True)
        return Response(serializer.data)
