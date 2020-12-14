from django.shortcuts import render
from products.views import get_products_view
# Create your views here.

def home_view(request, *args,**kwargs):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['x']
        context['query'] = str(query)

    presults = get_products_view(query)
    context ['presults'] = presults
    return render(request, "home.html", context )

def cart_view(request):
    context = {}
    return render(request, 'cart.html', context)
    