from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from apps.models import Order
from apps.serializers import OrderSerializer


@extend_schema(tags=['order'])
class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
