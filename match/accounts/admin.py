from django.contrib import admin
from .models import *
@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    pass
    # fields = '__all__'
# @admin.register(Order)
# class orderAdmin(admin.ModelAdmin):
#     inlines = [OrderInLine]

# admin.site.register(OrderItem)
