from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    TaskerAvailabilityViewSet,
    TaskerSkillViewSet,
    TimeslotViewSet,
    BusinessPhotoViewSet,
)

router = DefaultRouter()
router.register("timeslot", TimeslotViewSet)
router.register("taskeravailability", TaskerAvailabilityViewSet)
router.register("businessphoto", BusinessPhotoViewSet)
router.register("taskerskill", TaskerSkillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
