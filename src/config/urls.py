from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from src.modules.mentoring.handlers import router as mentoring_router

api = NinjaAPI(
    title="Mentora backend", description="This is mentora's challenge API RESTFUL"
)


api.add_router("mentoring", mentoring_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
