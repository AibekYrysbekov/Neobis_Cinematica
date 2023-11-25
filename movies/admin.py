from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Discount)
admin.site.register(Cinema)
admin.site.register(Feedback)
admin.site.register(Ticket)
admin.site.register(PurchaseHistory)