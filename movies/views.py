from datetime import datetime

from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie, Ticket, Cinema
from .serializers import *


class MovieAPIListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        movies = self.get_queryset()
        serializer = self.serializer_class(movies, many=True)
        return Response({"data": serializer.data, "message": "Список фильмов успешно получен"},
                        status=status.HTTP_200_OK)


class MovieAPICreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "Фильм успешно создан"},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "message": "Ошибка при добавлении фильма"},
                        status=status.HTTP_400_BAD_REQUEST)


class MovieAPIUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAdminUser,)


class TicketAPIListView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        tickets = self.get_queryset()
        serializer = self.serializer_class(tickets, many=True)
        return Response({"data": serializer.data, "message": "Список билетов успешно получен"},
                        status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = request.user
            ticket = serializer.instance
            purchase_amount = ticket.amount
            discount, created = Discount.objects.get_or_create(user=user)
            discount.apply_discount(purchase_amount)
            return Response({"data": serializer.data, "message": "Билет успешно создан"},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "message": "Ошибка при создании билета"},
                        status=status.HTTP_400_BAD_REQUEST)


class CinemaAPIListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = TicketSerializer
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


class DiscountAPIListView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = (IsAdminUser,)
