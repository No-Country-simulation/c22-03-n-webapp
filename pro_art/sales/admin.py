from django.contrib import admin
from .models import (
    Order,
    OrderDetail,
    Invoice,
    InvoiceDetail,
    Payment,
)


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderDetailAdmin(admin.ModelAdmin):
    pass


class InvoiceAdmin(admin.ModelAdmin):
    pass


class InvoiceDetailAdmin(admin.ModelAdmin):
    pass


class PaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
admin.site.register(Payment, PaymentAdmin)
