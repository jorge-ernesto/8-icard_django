'''
Creando el CRUD de pedidos
'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from orders.models import Order
from orders.api.serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class OrderApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class   = OrderSerializer
    queryset           = Order.objects.all().order_by('table', 'id')

    # Filtros
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['table', 'status', 'close']
    ordering_fields = '__all__'
