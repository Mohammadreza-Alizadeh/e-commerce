from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='RegisterView'),
    path('login/', views.LoginView.as_view(), name='LoginView'),
    path('logout/', views.LogoutView.as_view(), name='LogoutView'),
    path('dashboard/', views.DashboardView.as_view(), name='DashboardView'),
]
