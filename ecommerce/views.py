from django.shortcuts import render, get_object_or_404, redirect
from django import views
from django.http import HttpResponse
from .models import Product
from .cart import Cart
from .forms import AddToCartForm, DeleteFromCartForm


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
        return redirect('ecommerce:HomeView')
    
class DeleteFromCart(views.View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart(request)
        cart.delete(product)

        return redirect('ecommerce:CartView')
        