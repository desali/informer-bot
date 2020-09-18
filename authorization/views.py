from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from authorization.forms import LoginForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'authorization/login.html'

    def get(self, request, *args, **kwargs):
        admin = LoginForm()

        return render(request, self.template_name, {
            'form': admin
        })

    def post(self, request, *args, **kwargs):
        admin = LoginForm(request.POST)

        if admin.is_valid():
            username = admin.cleaned_data['username']
            password = admin.cleaned_data['password']

            result = authenticate(username=username, password=password)
            if result:
                login(request, result)
                return redirect('home')
            else:
                return render(request, self.template_name, {
                    'form': admin
                })
        else:
            return render(request, self.template_name, {
                'form': admin
            })


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect('login')
