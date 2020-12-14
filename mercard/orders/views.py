from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

from .forms import OrderForm
from products.models import Products
from .models import Order


@login_required
def order_checkout_view(request):  #atualiza os status das orders para 'paid'
    user = request.user
    orders= Order.objects.filter(user=user,status='created')
    for x in orders:
        x.mark_paid(save=False)
        x.save()
    return redirect("/")

def Pay(request):  #redireciona para a pagina de pagamento
    return render(request,"checkout.html")

@login_required
def CreateOrder(request):  #cria orders a partir da pagina do produto
    quant = int(request.GET['quant'])
    print('quant',quant)
    user = request.user
    print('user',user)
    products_id = request.GET['product_id']
    print('products_id',products_id)
    products = Products.objects.get(ID=products_id)
    print('products',products)
    #if Order.objects.filter(user=user,status=created,products=products)
    if quant < products.quantity:
        order = Order.objects.create(products=products, user=user, quantidade_comprada=quant)
    else:
        order = Order.objects.create(products=products, user=user, quantidade_comprada=products.quantity)
    print('sem erros aqui')
    orders = Order.objects.filter(user=user,status='created')
    print(orders)
    params = {'orders': orders, 'search':user, 'total': 0, 'items': 0}
    print(params)

    for x in params['orders']:
        params['total'] += x.calculate()
        params['items'] += x.quantidade_comprada

    return render(request, 'cart.html', params) 

@login_required
def DeleteOrder(request):
    order_id = int(request.GET['ID'])
    order = Order.objects.filter(ID=order_id)
    user = request.user
    orders = Order.objects.filter(user=user,status='created')
    print(orders)
    params = {'orders': orders, 'search':user, 'total': 0, 'items': 0}
    print(params)

    for x in params['orders']:
        params['total'] += x.calculate()
        params['items'] += x.quantidade_comprada

    return render(request, 'cart.html', params) 


@login_required
def SearchOrder(request):   #filtra os pedidos de um usuário para exebir em seu carrinho e calcula total de items e seu valor conjunto
    srh = request.user
    orders = Order.objects.filter(user=srh,status='created')
    print(orders)
    params = {'orders': orders, 'search':srh, 'total': 0, 'items': 0}
    print(params)

    for x in params['orders']:
        params['total'] += x.calculate()
        params['items'] += x.quantidade_comprada

    return render(request, 'cart.html', params)
