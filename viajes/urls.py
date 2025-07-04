from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ViajeViewSet, SolicitudViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'viajes', ViajeViewSet)
router.register(r'solicitudes', SolicitudViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
