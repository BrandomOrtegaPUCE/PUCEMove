from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ViajeViewSet, SolicitudViewSet, LoginView, perfil_usuario

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'viajes', ViajeViewSet)
router.register(r'solicitudes', SolicitudViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/perfil/', perfil_usuario, name='perfil_usuario'),
]
