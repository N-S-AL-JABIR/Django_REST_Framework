from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, patientregisterapiview ,activate_account, UserloginAPIView, UserlogoutAPIView

router = DefaultRouter()
router.register("list", PatientViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", patientregisterapiview.as_view(), name="register"),
    path("login/", UserloginAPIView.as_view(), name="login"),
    path("logout/", UserlogoutAPIView.as_view(), name="logout"),
    path("activate/<uidb64>/<token>/",activate_account, name="activate"),
]
