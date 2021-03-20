from django.urls import re_path, include

from .views import RegistrationAPIView, LoginAPIView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'login', LoginAPIView, basename='login')
router.register(r'register', RegistrationAPIView, basename='register')

urlpatterns = router.urls