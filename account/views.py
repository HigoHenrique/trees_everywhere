from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

@login_required(login_url='account:login')
def index(req):
    return render(
        req,
        'account/index.html',
    )

def login_view(req):
     form = AuthenticationForm(req)
     if req.method == 'POST':
        form =AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(req,user)
            messages.error(req, 'Logado com sucesso')
            return redirect('tree:index')
        messages.error(req, 'Login inválido')

     return render(
        req,
        'account/login.html',
        {
            'form':form
        }
    )

@login_required(login_url='account:login')
def logout_view(req):
    auth.logout(req)
    return redirect('account:login')