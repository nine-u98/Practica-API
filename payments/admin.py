from django.contrib import admin
from .models import Payment, Payment_user, Expired_payment, Pagos


# Register your models here.
admin.site.register(Pagos)
admin.site.register(Payment)
admin.site.register(Payment_user)
admin.site.register(Expired_payment)
