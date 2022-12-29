from rest_framework import serializers
from .models import Payment, Pagos, Payment_user, Expired_payment


# V1 Serializer
class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'


# V2 Serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = 'users', 'payment_date'


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = 'user_id', 'payment_date', 'expiration_date'


class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payment
        fields = '__all__'