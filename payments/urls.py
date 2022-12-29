from django.urls import re_path
from rest_framework import routers
from .views import PagoViewSet,PaymentsViewSet, ExpiredPaymentsViewSet, PaymentUserViewSet


router=routers.DefaultRouter()
router.register(r'v1/pagos', PagoViewSet)
router.register(r'v2/payment', PaymentsViewSet)
router.register(r'v2/payment-user', PaymentUserViewSet)
router.register(r'v2/expired-payments', ExpiredPaymentsViewSet)

urlpatterns=[]

urlpatterns += router.urls