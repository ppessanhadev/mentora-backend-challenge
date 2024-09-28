from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.throttling import AnonRateThrottle

from src.modules.mentoring.handlers import router as mentoring_router
from src.modules.feedback.handlers import router as feedback_router

api = NinjaAPI(
    title="Mentora backend",
    description="This is mentora's challenge API RESTFUL",
    throttle=[AnonRateThrottle("8/s")],
)


api.add_router("mentoring", mentoring_router)
api.add_router("feedback", feedback_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
