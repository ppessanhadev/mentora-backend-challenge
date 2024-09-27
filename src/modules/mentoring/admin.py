from .models import MentoringModel
from django.contrib import admin


@admin.register(MentoringModel)
class MentoringAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price")
