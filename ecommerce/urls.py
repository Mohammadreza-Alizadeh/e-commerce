from django.urls import path

from . import views 

app_name = 'ecommerce'

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('cart/', views.CartView.as_view(), name='CartView'),
    path('cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='AddToCartView'),
    path('cart/del/<int:product_id>/', views.DeleteFromCart.as_view(), name='DeleteFromCartView'),
]
