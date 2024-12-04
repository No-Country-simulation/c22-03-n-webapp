from django.contrib import admin
from .models import Users, Type_user
# Register your models here.


class UserProartAdmin(admin.ModelAdmin):
    pass


class ProviderAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


class Type_userAdmin(admin.ModelAdmin):
    pass


admin.site.register(Type_user, Type_userAdmin)
admin.site.register(Users, UserProartAdmin)
