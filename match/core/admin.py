from django.contrib import admin
from accounts.models import *
from .models import User

class OrderInLine(admin.TabularInline):
    model = OrderItem
    fields = ['order']
@admin.register(User)
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderInLine]
# admin.site.register(User)

