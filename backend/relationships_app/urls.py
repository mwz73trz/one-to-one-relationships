from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('admins', AdminViewSet, basename='admin')
router.register('corporations', CorporationViewSet, basename='corporation')
router.register('managers', ManagerViewSet, basename='manager')

urlpatterns = [
    path('', include(router.urls)),
]