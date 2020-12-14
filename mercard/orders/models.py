from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save

# Create your models here.

from products.models import Products

User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)

class Order(models.Model):  
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null= True, on_delete = models.SET_NULL)
    products = models.ForeignKey(Products, null= True, on_delete = models.SET_NULL)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created')
    subtotal = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
    quantidade_comprada = models.IntegerField(default = 1)
    total = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
    paid = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
    shipping_address = models.TextField(blank=True, null= True)
    billing_address = models.TextField(blank=True, null=True)
    quantity_updated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def mark_paid(self, custom_amount=None, save=False): #atualiza o status da order para 'paid'
        paid_amount = self.total
        self.paid = paid_amount
        self.status = 'paid'
        self.save()
        if not self.quantity_updated and self.products:
            print('products',self.products)
            self.products.item_sold(count=self.quantidade_comprada,save=True)
            self.quantity_updated = True
        return self.paid

    def calculate(self, save=False):    #calcula a quantidade total de items e o valor final de um pedido.
        if not self.products:
            return {}
        subtotal = self.products.price
        quantidade_comprada_rate = Decimal(self.quantidade_comprada)
        total = Decimal(subtotal * quantidade_comprada_rate)
        totals = {
            "subtotal": subtotal,
            "quantidade_comprada": self.quantidade_comprada,
            "total": total
        }
        for k,v in totals.items():
            setattr(self, k, v)
            if save == True:
                self.save()
        return total

def order_pre_save(sender, instance, *args, **kwargs):
    instance.calculate(save=False)

pre_save.connect(order_pre_save, sender=Order)