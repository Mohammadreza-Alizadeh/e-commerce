from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django import http, views
from django.http import HttpResponse
from .models import Product, Order
from .cart import Cart
from .forms import AddToCartForm, DeleteFromCartForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(views.View):

    template_name = 'ecommerce/home.html' 

    def get(self, request):
        products = Product.objects.all()

        data_pack = {}
        
        for product in products:
            to_url = 'cart/add/' + str(product.id) + '/'
            data_pack[product] = AddToCartForm(action_url = to_url)
            

        context = {
            'data_pack' : data_pack,
        }

        return render(request, self.template_name, context)



class CartView(views.View):

    template_name = 'ecommerce/cart.html'  

    def get(self, request):
        return render(request, self.template_name)


class AddToCartView(views.View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = AddToCartForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            messages.success(request, 'Added To your Cart, You can see and pay for it in cart page you can access it from navbar')
        return redirect('ecommerce:HomeView')
    
class DeleteFromCart(views.View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart(request)
        cart.delete(product)

        return redirect('ecommerce:CartView')
        

class PayView(views.View):

    def dispatch(self, request ,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, f'you need to Login First')                
            return redirect('ecommerce:CartView')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        cart = Cart(request)

        for product_id , product in cart:
            p = get_object_or_404(Product, pk=product_id)
            if p.stock < product['quantity'] :
                messages.error(request, f'you ordered product "{p.title}" more than current stock')                
                return redirect('ecommerce:CartView')

        for product_id , product in cart:
            p = get_object_or_404(Product, pk=product_id)
            o = Order.objects.create(
                profile = request.user.profile,
                product = p,
                quantity = product['quantity'],
            )   
            o.mark_as_payed()     
            p.decrease_stock(o.quantity)

        cart.empty()
        messages.success(request, 'Successfull, you can see list of products you bought on User Dashboard')
        return redirect('ecommerce:CartView')








# this view is for producing initial datas you can delete this and it's url path in urls.py
# if you want to create products manually
from .produce_data import produce_data

class ProduceDataView(views.View):

    def get(self, request):
        produce_data.produce()
        return redirect('ecommerce:HomeView')
