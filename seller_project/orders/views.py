from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, View
from .models import OrdersModel
from .forms import OrdersForm
from seller_project.markets.models import MarketModel
from seller_project.products.models import ProductsModel
from seller_project.finance.models import FinanceModel
from ozon_api.api import Ozon
import os
from dotenv import load_dotenv
from datetime import datetime
from django.urls import reverse_lazy
from django.db import transaction


load_dotenv()


class TimeConvert:
    def __init__(self, date):
        self.date = date
        self.convert(self.date)

    def convert(self, date):
        self.date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        self.date = self.date.strftime('%Y-%m-%d')
        return self.date


class UpdateOrdersModel:
    """ Fetch new order by API """
    api_key = os.getenv('OZON_API')
    client_id = os.getenv('CLIENT_ID')
    data = Ozon(api_key, client_id)
    for order in data.get_orders()['result']['postings']:
        data.get_order(order['posting_number'])
        date = TimeConvert(order['shipment_date']).date
        if not OrdersModel.objects.filter(order_number=order['posting_number']):
            with transaction.atomic():
                market_object, _ = MarketModel.objects.get_or_create(
                    name='ozon',
                )
                product_object, _ = ProductsModel.objects.get_or_create(
                    name=order['products'][0]['name'],
                )
                FinanceModel.objects.create(
                    product_name=product_object,
                    order_number=OrdersModel.objects.create(
                        market=market_object,
                        product_name=product_object,
                        delivery_time=date,
                        order_number=order['posting_number'],
                    ),
                    price=data.price,
                    sale_commission=0,
                    processing_and_delivery=0,
                )


class Index(UpdateOrdersModel, ListView):
    """ Current orders """
    model = OrdersModel
    template_name = 'orders/index.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return OrdersModel.objects.all().exclude(is_finished=1).exclude(canceled=1).order_by('delivery_time')


class CompleteOrder(View):
    """ Set complete flag to order """
    def get(self, request, *args, **kwargs):
        order = OrdersModel.objects.get(id=kwargs['pk'])
        order.is_finished = True
        order.actually_finished = datetime.today().strftime('%Y-%m-%d')
        order.save()
        return redirect(reverse_lazy('index_page'))


class PrintedOrder(View):

    def get(self, request, *args, **kwargs):
        order = OrdersModel.objects.get(id=kwargs['pk'])
        order.is_printed = True
        order.save()
        return redirect(reverse_lazy('index_page'))


class DeleteOrder(DeleteView):
    model = OrdersModel
    template_name = 'orders/delete.html'
    success_url = reverse_lazy('index_page')


class ViewOrder(DetailView):
    model = OrdersModel
    template_name = 'orders/detail.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        return OrdersModel.objects.get(id=self.kwargs['pk'])


class CancelOrder(View):
    """ Set canceled order flag """
    def get(self, request, *args, **kwargs):
        order = OrdersModel.objects.get(id=kwargs['pk'])
        order.canceled = True
        order.save()
        return redirect(reverse_lazy('index_page'))


class AllOrders(ListView):
    """ Show all orders """
    model = OrdersModel
    template_name = 'orders/all_orders.html'
    context_object_name = 'orders'
