from django.contrib import admin
from .models import Users
# Register your models here.


class UserProartAdmin(admin.ModelAdmin):
    pass


class ProviderAdmin(admin.ModelAdmin):
    pass


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Users, UserProartAdmin)


