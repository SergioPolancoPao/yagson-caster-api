from django.urls import path, include
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter,
)
from .views import ServerViewSet

router = ExtendedDefaultRouter()
servers_router = router.register("servers", ServerViewSet, basename="server")

urlpatterns = [path("", include(router.urls))]