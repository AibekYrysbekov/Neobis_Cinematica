from django.db import models

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    add_date = models.DateTimeField(auto_created=True)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    schedule = models.TextField()
    contact_info = models.CharField(max_length=255)


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    room_type = models.CharField(max_length=100)


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    showtime_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    row_number = models.PositiveIntegerField()
    is_reserved = models.BooleanField(default=False)


class Ticket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    showtime = models.ForeignKey('Showtime', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100    )


class Feedback(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.TextField(max_length=500)


class Discount(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
