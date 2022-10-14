from django.contrib import admin
from .models import Customer,Order

class OrderInLine(admin.TabularInline):
    model = Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [OrderInLine]

