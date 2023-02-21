import os

from django.db.models import Sum

from seller_project.finance.models import FinanceModel
from django.views.generic import ListView
from ozon_api import Ozon
from dotenv import find_dotenv, load_dotenv
from django.db.models.functions import TruncMonth
from django.db.models import Q


load_dotenv(find_dotenv())


class UpdateFinanceModel:
    finance = Ozon(os.getenv('OZON_API'), os.getenv('CLIENT_ID'))
    for order in FinanceModel.objects.all().filter(sale_commission=0).filter(order_number__canceled=False):
        finance.get_finance(order.order_number.order_number)
        # order.price = finance.price
        order.processing_and_delivery = finance.processing_and_delivery
        order.sale_commission = finance.sale_commission
        order.save()


class FinanceView(UpdateFinanceModel, ListView):
    model = FinanceModel
    template_name = 'finance/index.html'
    context_object_name = 'orders'


class FinanceReport(ListView):
    model = FinanceModel
    template_name = 'finance/report.html'
    context_object_name = 'reports'

    def get_queryset(self):
        queryset = FinanceModel.objects.exclude(order_number__canceled=True).annotate(month=TruncMonth("order_number__delivery_time")).values("month")
        queryset = queryset.annotate(current_profit=Sum("price", filter=~Q(sale_commission=0)))
        queryset = queryset.annotate(excpected_profit=Sum("price")).order_by("-month")
        return queryset
