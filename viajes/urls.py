from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViajeViewSet, SolicitudViewSet, LoginView, perfil_usuario, registro_usuario, UserViewSet

router = DefaultRouter()
router.register(r'viajes', ViajeViewSet, basename='viaje')
router.register(r'solicitudes', SolicitudViewSet, basename='solicitud')
router.register(r'users', UserViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),              # <-- Sin 'api/' aquí
    path('login/', LoginView.as_view(), name='api_login'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('registro/', registro_usuario, name='registro_usuario'),
]
