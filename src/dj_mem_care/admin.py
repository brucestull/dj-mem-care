from django.contrib import admin

from .models import Confabulation


@admin.register(Confabulation)
class ConfabulationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "updated_at")
    search_fields = ("text",)
    readonly_fields = ("created_at", "updated_at")
