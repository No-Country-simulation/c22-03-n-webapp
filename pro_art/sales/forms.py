from django.forms import ModelForm

from .models import OrderDetail


class OrderDetailUpdateQuantityForm(ModelForm):

    class Meta:
        model = OrderDetail
        fields = ('quantity', )
