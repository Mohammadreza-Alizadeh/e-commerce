from django.urls import path

from . import views 

app_name = 'ecommerce'

urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('cart/', views.CartView.as_view(), name='CartView'),
    path('cart/add/<int:product_id>/', views.AddToCartView.as_view(), name='AddToCartView'),
    path('cart/del/<int:product_id>/', views.DeleteFromCart.as_view(), name='DeleteFromCartView'),
    path('cart/pay', views.PayView.as_view(), name='PayView'),

    # this a Product instance creater, you can use this to create some fake data for test 
    # consider deleting this and it's view from views.py if you want to create products manualy 
    path('produce_data_for_test/', views.ProduceDataView.as_view(), name='ProduceDataView'),
]
