from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, PaymentForm
from .models import Payment, Earning
from datetime import datetime, timedelta, date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.db.models.expressions import F
from mainapp.models import WalletID
import math, random


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful")
            
            earning = Earning.objects.create(user=request.user)
            profile = Payment.objects.create(user=request.user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    profile = Payment.objects.all()
    wallet_id = WalletID.objects.last()
    days_left = 0
    if request.user.registration:
        payment = Payment.objects.get(user=request.user)
    
        days_left = (datetime.now().date() - payment.date.date()).days 
    else:
        days_left = 0
    earning = Earning.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'profile': profile, 'wallet_id':wallet_id, 'earning':earning, 'days_left': days_left} )


@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            paid = form.save(commit=False)
            paid.user = request.user
            paid.save()
            messages.success(request, "Account Activated, waiting for approval")
    else:
        form = PaymentForm()
        return render(request, 'activation.html', {'form': form})
    