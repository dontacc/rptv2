from django.contrib import admin
from . import models


@admin.register(models.PrivacyPolicy)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RefundPolicy)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contact)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.QandASupport)
class CustomerAdmin(admin.ModelAdmin):
    pass
