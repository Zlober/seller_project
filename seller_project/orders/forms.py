from django import forms
from .models import OrdersModel


class OrdersForm(forms.ModelForm):

    class Meta:
        model = OrdersModel
        fields = (
            'actually_finished',
            'is_finished',
        )
        labels = {
            'actually_finished': 'Фактическая дата отправки',
            'is_finished': 'Отправлено',
        }
