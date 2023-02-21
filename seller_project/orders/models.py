from django.db import models
from seller_project.markets.models import MarketModel
from seller_project.products.models import ProductsModel


class OrdersModel(models.Model):
    market = models.ForeignKey(MarketModel, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    delivery_time = models.DateField(null=False)
    order_number = models.CharField(max_length=255, null=False, unique=True)
    is_finished = models.BooleanField(default=False)
    actually_finished = models.DateField(null=True)
    canceled = models.BooleanField(default=False)
    is_printed = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number
