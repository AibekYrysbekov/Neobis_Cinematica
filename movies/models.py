from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=500)
    add_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    schedule = models.CharField(max_length=30)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    room_type = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    showtime_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Время сеанса: {self.showtime_date.strftime("%Y-%m-%d %H:%M")} Цена: {self.price} сом'


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    row_number = models.PositiveIntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'Ряд: {self.row_number}, Место: {self.seat_number}'


class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ManyToManyField(Seat)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Ticket ID: {self.id}'

    def save(self, *args, **kwargs):
        if not self.id or 'quantity' in kwargs:
            showtime_price = self.showtime.price
            total_amount = showtime_price * self.quantity
            self.amount = total_amount
        super().save(*args, **kwargs)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user.username}'

    class Meta:
        ordering = ['-created_at']
        # unique_together = ('user',)


class Discount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    last_purchase_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def apply_discount(self, amount_spent):
        self.last_purchase_amount = amount_spent
        self.discount_percentage += 0.03 * amount_spent
        self.save()

    def __str__(self):
        return f'{self.user.username} Ваша экономия: {self.discount_percentage}%'


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Purchase history for {self.user.username}'
