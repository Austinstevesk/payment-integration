from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
import requests

from woot_paypal import models
from .forms import UserRegisterForm
from mpesa_app import  models
#from ..mpesa_app import  models

import json

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

def mpesa_payment(request):
    url = "https://chatndovu.herokuapp.com/mpesa/submit/"
    
    # if request.method == 'POST':
    #     phone = request.POST.get('phone-number')
    #     print(request)
    #     # print(request.POST.get('phone-number'))
    #     # header = {
    #     #     "Content-Type":"application/json",
    #     # }
    #     # payload = {
    #     #     "phone_number" : phone,
    #     #     "amount": 1,
    #     #     "paybill_account_number": 4001637
    #     # }
        
    #     req = requests.post(url, phone_number=phone, amount=1,paybill_account_number=4001637)#data=json.dumps(payload), headers=header, params=request.POST)
    #     if req.status_code == 200:
    #         return HttpResponse("Payment Successful")
    #     return HttpResponse("Payment Unsuccessful")
    # else:
    #     return render(request, 'woot_paypal/payment_card.html')



def checkout(request):
    return render(request, 'woot_paypal/checkout.html')

def payment(request):
    if request.method == 'POST':
        url = "https://chatndovu.herokuapp.com/mpesa/submit/"
        print(request)
        print(request.POST.get('phone-number'))
        phone_number = request.POST.get('phone-number')
        header = {
           "Content-Type":"application/json",
        }
        payload = {
            "phone_number" : phone_number,
            "amount": 1,
            "paybill_account_number": 4001637
        }
        
        req = requests.post(url, data=json.dumps(payload), headers=header)
        if req.status_code == 200:
            trans_resp = req.json()
            print(trans_resp["transaction_id"])
            print(models.PaymentTransaction.objects.all())
            return HttpResponse("Payment Successful")
        print(req.status_code)
        return HttpResponse("Payment Unsuccessful")
    else:

        return render(request, 'woot_paypal/payment_card.html')

def payment_complete(request):
    body = json.loads(str(request.body))
    print('Body:', body)
    return JsonResponse('Payment completed!', safe=False)

def home(request):
    return render(request, 'woot_paypal/index.html')




