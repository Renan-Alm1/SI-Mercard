from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, JsonResponse, Http404
# Create your views here.

from .models import Products
from .forms import ProductsForm

def product_det_view(request, pk): #view dos detalhes do produto
    try:
        obj = Products.objects.get(ID = pk) #pega o id do produto que está na url
    except Products.DoesNotExist: #produto não encontrado
        raise Http404
    details = { 
    'ID' : pk,
    'user' : obj.user,
    'title' : obj.title,
    'images' :  obj.images,
    'price' : obj.price, 
    'tipo' : obj.tipo,
    'country': obj.country,
    'quantity' : obj.quantity,
    'Language' : obj.Language,
    'Card_condition' : obj.Card_condition,
    'Game_condition' : obj.Game_condition,
    }

    return render(request, "Products/detail.html", details)

@staff_member_required #apenas vendedores podem colocar produtos a venda
def product_forms_view(request,*args,**kwargs): #forms para inserção de novos produtos
    
    M_forms = ProductsForm() #método get, não é seguro
    if request.method == "POST": # checa se é POST, mais seguro
        M_forms = ProductsForm(request.POST or None, request.FILES or None)
        if M_forms.is_valid(): # checa mais uma vez por segurança
            obj =M_forms.save(commit=False)
            images = request.FILES['images'] # imagem atribuida ao produto
            obj.images = images
            obj.save()
            print('Adicionado com sucesso')
            return redirect("/") #redireciona à home
    context = {
        "form" : M_forms
    }
    return render(request, "Products/product_form.html", context)

def get_products_view(query = None):
    queryset = []
    queries = query.split(" ")
    for x in queries:
        prod = Products.objects.filter(
            Q(title__icontains = x)
        ).distinct()
        for y in prod:
            queryset.append(y)
    return list(set(queryset))

def SearchPage(request): #pagina de pesquisa
    srh = request.GET['query']
    products = Products.objects.filter(title__icontains=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'search page.html', params)

def TypeYGOC(request): #pagina de Yu-gi-Oh
    srh = 'YGOC'
    products = Products.objects.filter(tipo=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'search page.html', params)
def TypeMC(request):  #pagina de Magic
    srh = 'MGC'
    products = Products.objects.filter(tipo=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'search page.html', params)
def TypePKC(request):  #pagina de Pokemon
    srh = 'PKMNC'
    products = Products.objects.filter(tipo=srh)
    params = {'products': products, 'search':srh}
    return render(request, 'search page.html', params)