from django.contrib import admin
from django.urls import path
from DRF import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("stinfo/", views.student_detail),
]
