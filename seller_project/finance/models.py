from django.db import models
from seller_project.products.models import ProductsModel
from seller_project.orders.models import OrdersModel


class FinanceModel(models.Model):
    product_name = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    order_number = models.ForeignKey(
        OrdersModel,
        on_delete=models.CASCADE,
    )
    price = models.BigIntegerField(null=True)
    sale_commission = models.BigIntegerField(null=True)
    processing_and_delivery = models.BigIntegerField(null=True)


class FinanceMonthModel(models.Model):
    date = models.DateField(null=False)
    current_profit = models.BigIntegerField()
    expected_profit = models.BigIntegerField()
