from django.urls import path
from .views import *

urlpatterns = [

    path('movie-list', MovieAPIListView.as_view(), name='movie-list'),
    path('movie-create', MovieAPICreateView.as_view(), name='movie-create'),
    path('movie-detail/<int:pk>', MovieAPIUpdateView.as_view(), name='movie-detail'),
    path('ticket/', TicketAPIListView.as_view(), name='ticket-list-create'),
    path('cinema/', CinemaAPIListView.as_view(), name='cinema-list-create'),
    path('room/', RoomAPIListView.as_view(), name='room-list-create'),
    path('showtime/', ShowtimeAPIListView.as_view(), name='showtime-list-create'),
    path('seat/', SeatAPIListView.as_view(), name='seat-list-create'),
    path('feedback/', FeedbackAPIListView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>', FeedbackAPIDeleteView.as_view(), name='feedback-detail'),
    path('purchase-history', UserPurchaseHistoryView.as_view(), name='purchase-history-list'),
    path('discount', DiscountAPIListView.as_view(), name='discount-list-create'),

]
