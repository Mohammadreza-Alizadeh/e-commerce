from django.urls import path

from . import views 

app_name = 'ecommerce'

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='AddToCartView')
]
