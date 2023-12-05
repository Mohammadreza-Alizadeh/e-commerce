from django.shortcuts import render
from django import views
from django.http import HttpResponse


# Create your views here.
class HomeView(views.View):


    template_name = 'ecommerce/home.html' 
    def get(self, request):
        return render(request, self.template_name)