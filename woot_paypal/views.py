from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import UserRegisterForm

import json
from .models import User
# Create your views here.

def register(request):
    if request == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('https://chat.ndovucloud.com/app/auth/login')
        context = {
            'register_form': form
        }

    else:
        form = UserRegisterForm()
        context = {
            'register_form': form
        }

    return render(request, 'woot_paypal/signup.html')


def checkout(request):
    return render(request, 'woot_paypal/checkout.html')

def payment(request):
    return render(request, 'woot_paypal/payment_card.html')

def payment_complete(request):
    body = json.loads(request.body)
    print('Body:', body)
    return JsonResponse('Payment completed!', safe=False)
