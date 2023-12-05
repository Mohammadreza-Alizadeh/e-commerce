from django.shortcuts import render, redirect
from django import views
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from .mixins import LimitLoginUser
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages


class RegisterView(views.View):
        
    register_view_name = 'accounts:RegisterView'
    home_view_name = 'ecommerce:HomeView'
    template_name = 'accounts/formTemplate.html'
    
    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form' : form,
            'title' : 'Register',
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass



class LoginView(LimitLoginUser, views.View):

    login_view_name = 'accounts:LoginView'
    home_view_name = 'ecommerce:HomeView'
    template_name = 'accounts/formTemplate.html'
    
    def get(self, request):
        form = UserLoginForm()

        context = {
            'form' : form,
            'title' : 'Login'
        }
        return render(request, self.template_name, context)

    def post(self , request):
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password']) 
            if user is not None :
                login(request, user)
                return redirect(self.home_view_name)
            messages.error(request, 'your email or password is wrong', 'danger')
            return redirect(self.login_view_name)

        messages.error(request, 'your request wasn\'t valid', 'danger')
        return redirect(self.login_view_name)

class LogoutView(LoginRequiredMixin, views.View):
    
    def get(self, request):
        logout(request)
        return redirect('accounts:LoginView')