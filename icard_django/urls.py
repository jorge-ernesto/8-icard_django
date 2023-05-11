"""icard_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# Configurando la documentación de la API
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Creando el CRUD de usuarios
from users.api.router import router_user
# Creando el CRUD de categorias
from categories.api.router import router_category
# Creando el CRUD de productos
from products.api.router import router_product
# Creando el CRUD de mesas
from tables.api.router import router_table
# Creando el CRUD de pedidos
from orders.api.router import router_order

# Configurando la documentación de la API
schema_view = get_schema_view(
    openapi.Info(
        title="iCard - ApiDoc",
        default_version='v1',
        description="Documentación de la API de iCard",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jorge.cywdt@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Configurando la documentación de la API
    path('docs/'  , schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0)  , name='schema-redoc'),

    # Creando endpoint de login con JWT en Django
    # Creando endpoint para obtener los datos personales
    # include('users.api.router') llama a la aplicacion "users", luego al paquete "api" y al fichero "router",
    # del fichero "router" obtiene automaticamente obtiene la variable "urlpatterns",
    # del mismo modo como si estuvieramos usando un app cualquiera ----> path('', include('mainapp.urls'))
    path('api/', include('users.api.router')),
    # Creando el CRUD de usuarios
    path('api/', include(router_user.urls)),
    # Creando el CRUD de categorias
    path('api/', include(router_category.urls)),
    # Creando el CRUD de productos
    path('api/', include(router_product.urls)),
    # Creando el CRUD de mesas
    path('api/', include(router_table.urls)),
    # Creando el CRUD de pedidos
    path('api/', include(router_order.urls)),
]

# Ruta para cargar imagenes
if settings.DEBUG == True:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
