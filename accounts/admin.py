from django.contrib import admin
from .models import Order

class OrderInLine(admin.TabularInline):
    model = Order


