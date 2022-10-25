from django.contrib import admin
from .models import Collection,ContactUsQuestions
#
# class OrderInLine(admin.TabularInline):
#     model = Order

@admin.register(ContactUsQuestions)
class CustomerAdmin(admin.ModelAdmin):
    pass
@admin.register(Collection)
class CustomerAdmin(admin.ModelAdmin):
    pass