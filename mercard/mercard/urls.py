"""mercard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from pages.views import home_view, cart_view
from products.views import product_det_view, product_forms_view, SearchPage, TypeYGOC, TypeMC, TypePKC 
from accounts.views import login_page, logout_view, register_page, registerstaff_view
from orders.views import order_checkout_view, SearchOrder, CreateOrder, Pay

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name= 'home'),
    path('product/<int:pk>', product_det_view),
    path('create/', product_forms_view),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_view, name="logout_view"),
    path('registerseller/', registerstaff_view, name = "register_seller"),
    path('ygosearch/', TypeYGOC, name='type_ygo'),
    path('mcsearch/', TypeMC, name='type_mc'),
    path('pksearch/', TypePKC, name='type_pkc'),
    path('search/', SearchPage, name='search_result'),
    path('adicao', CreateOrder, name='create_order'),
    path('pay/', Pay, name='pay'),
    path('checkout/', order_checkout_view, name = 'checkout'),
    path('cart/', SearchOrder, name='cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)