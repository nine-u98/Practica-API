from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.views import APIView
from .pagination import StandardResultsSetPagination
from .models import Payment, Pagos, Payment_user, Expired_payment
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .serializer import PaymentSerializer, PagosSerializer, PaymentUserSerializer, ExpiredPaymentsSerializer


# v1 Project
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagosSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['usuario', 'fecha_pago', 'servicios']
    throttle_classes = 'Pagos'


# v2 Project
class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['payment_date', 'amount']
    
    def get_permissions(self):
        if self.action in ['partial_update','update','destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]     
        return [permission() for permission in permission_classes]


class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id', 'service_id', 'paymentDate']
    http_method_names=['get','post']
    
    def get_permissions(self):
        if self.action in ["list", "create"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
   

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
    queryset = Expired_payment.objects.get_queryset().order_by('id')
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated,]
        else:
            permission_classes = [IsAdminUser,]
        return [permission() for permission in permission_classes]