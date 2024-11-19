from django.contrib import admin
from .models import User_proart, Provider, Customer
# Register your models here.


class UserProartAdmin(admin.ModelAdmin):
    pass


class ProviderAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(User_proart, UserProartAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Customer, CustomerAdmin)
