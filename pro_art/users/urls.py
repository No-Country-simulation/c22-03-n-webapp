from django.urls import path

from users.views.users.views import *





urlpatterns = [
 path('listado/', User_listView.as_view(), name='user_list'),
 path('registro/', User_createView.as_view(), name='user_add'),
]
