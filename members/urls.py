from django.urls import path, include
from rest_framework_extensions.routers import (
    ExtendedDefaultRouter,
)
from .views import MemberViewSet

router = ExtendedDefaultRouter()
members_router = router.register("members", MemberViewSet, basename="member")

urlpatterns = [path("", include(router.urls))]