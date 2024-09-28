from .models import FeedbackModel
from django.contrib import admin


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "message", "stars", "mentoring")
