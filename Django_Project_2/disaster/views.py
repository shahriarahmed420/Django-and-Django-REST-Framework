from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from django.urls import reverse 
from .forms import DonationForm, CrisisForm
from .models import Donation, Crisis 
from django.db.models import Sum 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def home(request):
    total_funds = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0 
    donations = Donation.objects.all().order_by('-date')
    recent_crisis = Crisis.objects.filter(is_approved=True)
    
    context = {
        'total_funds': total_funds, 
        'donation': donation, 
        'recent_crisis': recent_crisis
    }
    
    
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True 
            user.is_active = True
            user.save()
            login(request, user)
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()
        
    return render(request, 'register.html', {'form': form})


def register_volunteer(request):
    pass 


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    
    return redirect('login')


@login_required
def donation(request):    
    form = DonationForm()
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            if request.user.is_authenticated:
                donation.user = request.user
            donation.save()
            return redirect('donation')
    else:
        form = DonationForm()     

    total_funds = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0 
    donations = Donation.objects.all().order_by('-date')
    
    context = {
        'total_funds' : total_funds,
        'donations': donations,
        'form' : form
    }       
    
    return render(request, 'donation.html', context)


@login_required
def crisis(request):
    recent_crisis = Crisis.objects.filter(is_approved=True)
    
    severity_filter = request.GET.get('severity')
    if severity_filter:
        crisis = Crisis.objects.filter(severity = severity_filter)
    
    form = CrisisForm()
    
    if request.method == 'POST':
        form = CrisisForm(request.POST)
        if form.is_valid():
            crisis = form.save(commit=False)
            crisis.is_approved = False 
            crisis.save()
            return redirect('crisis')
    else:
        form = CrisisForm()
    
    return render(request, 'crisis.html', {'recent_crisis' : recent_crisis, 'form' : form})


@staff_member_required
def admin_crisis(request):
    recent_crisis = Crisis.objects.all()
    
    return render(request, 'admin_crisis.html', {'crises' : recent_crisis})


@staff_member_required
def admin_approve_crisis(request, crisis_id):
    crisis = get_object_or_404(Crisis, id=crisis_id)
    crisis.is_approved = True 
    crisis.save()
    
    return redirect('admin_crisis')


@staff_member_required
def admin_update_crisis(request, crisis_id):
    
    if request.method == 'POST':
        crisis = get_object_or_404(Crisis, id=crisis_id)
        status = request.POST.get('status')
        crisis.status = status
        crisis.save()
        
        return redirect('admin_crisis')