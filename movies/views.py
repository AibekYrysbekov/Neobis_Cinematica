from datetime import datetime

from django.db.models import Sum
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Ticket, Cinema
from .serializers import *


class MovieAPIListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)


class MovieAPICreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)


class MovieAPIUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)


class TicketAPIListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)


class CinemaAPIListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdminUser,)


class CinemaAPIListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = (IsAdminUser,)


class RoomAPIListView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUser,)


class ShowtimeAPIListView(generics.ListCreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = (IsAdminUser,)


class SeatAPIListView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAdminUser,)


class FeedbackAPIListView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        user_feedback = Feedback.objects.filter(user=self.request.user)
        if user_feedback.exists():
            raise serializers.ValidationError("Вы уже добавили фидбек")
        serializer.save(user=self.request.user)


class FeedbackAPIDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)


class UserPurchaseHistoryView(generics.ListCreateAPIView):
    serializer_class = PurchaseHistorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return PurchaseHistory.objects.filter(user=user)