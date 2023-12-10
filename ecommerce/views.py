from django.shortcuts import render, get_object_or_404, redirect
from django import views
from django.http import HttpResponse
from .models import Product
from .cart import Cart

# Create your views here.
class HomeView(views.View):

    template_name = 'ecommerce/home.html' 

    def get(self, request):
        products = Product.objects.all()

        context = {
            'products' : products,
        }

        return render(request, self.template_name, context)



class AddToCartView(views.View):

    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        cart = Cart(request)
        cart.add(product)
        return redirect('ecommerce:HomeView')
