'''
Creando el CRUD de usuarios
'''
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.api.views import UserApiViewSet, UserView  # viewsets significa conjuntos de vistas

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet
)

'''
Creando endpoint de login con JWT en Django
Creando endpoint para obtener los datos personales
'''
urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())
]
