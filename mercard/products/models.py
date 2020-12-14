from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Products(models.Model):
    mytipo = (
    ('GM', 'Console Game'),
    ('YGOC', 'Yugioh Card'),
    ('MGC', 'Magic Card'),
    ('PKMNC', 'Pokémon Card'),
    )

    mycardconditions = (
        ('NM','NM'),
        ('LP','LP'),
        ('MP','MP'),
        ('HP','HP'),
        ('D','D'),
        ('None','None'),
    )

    myGameconditions = (
        ('Nw','New'),
        ('LN','Like-New'),
        ('US','Used'),
        ('None','None'),
    )

    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null= True, on_delete = models.SET_NULL)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=100, decimal_places=2, default = 0.00)
    images = models.ImageField(upload_to ='products/')
    tipo = models.CharField(max_length=30, choices= mytipo)
    country = models.CharField(max_length=120)
    quantity = models.PositiveSmallIntegerField()
    Language = models.CharField(max_length=120)
    Card_condition = models.CharField(max_length=30, choices= mycardconditions)
    Game_condition = models.CharField(max_length=30, choices= myGameconditions)
    featured = models.BooleanField(default = False)
    
    @property
    def has_product(self):  #verifica se ha estoque do produto
        return self.quantity > 0 #boolean

    def item_sold(self, count=1, save=True):  #atualiza a quantidade disponivel do produto
        current_quantity = self.quantity
        if count > current_quantity:
            count = current_quantity
        current_quantity -= count
        self.quantity = current_quantity
        self.save()
        return self.quantity

    @property
    def order_btn_title(self):
        if not self.can_order:
            return "Indisponível"
        return "Comprar"