from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("specializations", views.SpecializationViewSet)
router.register("designations", views.DesignationViewSet)
router.register("available-times", views.AvailableTimeViewSet)
router.register("reviews", views.ReviewViewSet)
router.register("list", views.DoctorViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
