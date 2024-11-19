from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FarmerRegistrationForm, BuyerRegistrationForm, LoginForm
from django.contrib.auth.hashers import make_password


def register_farmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'farmer'
            user.is_approved = False  # Admin needs to approve
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Farmer registration successful! Pending admin approval.')
            return redirect('login')
    else:
        form = FarmerRegistrationForm()
    return render(request, 'users/register_farmer.html', {'form': form})

def register_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'buyer'
            user.is_approved = True  # Buyers don’t need approval
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Buyer registration successful! You can now log in.')
            return redirect('login')
    else:
        form = BuyerRegistrationForm()
    return render(request, 'users/register_buyer.html', {'form': form})


def register_farmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'farmer'  # Assign the farmer role
            user.is_approved = False  # Admin approval required
            user.password = make_password(form.cleaned_data['password'])  # Hash password
            user.save()
            messages.success(request, 'Registration successful! Pending admin approval.')
            return redirect('login')  # Redirect to login page
    else:
        form = FarmerRegistrationForm()
    return render(request, 'users/register_farmer.html', {'form': form})


def register_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'buyer'  # Assign the buyer role
            user.is_approved = True  # Buyers don’t need approval
            user.password = make_password(form.cleaned_data['password'])  # Hash password
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = BuyerRegistrationForm()
    return render(request, 'users/register_buyer.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'farmer':
                    return redirect('farmer_dashboard')  # Redirect to farmer dashboard
                elif user.role == 'buyer':
                    return redirect('buyer_dashboard')  # Redirect to buyer dashboard
                elif user.role == 'admin':
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

@login_required
def farmer_dashboard(request):
    return render(request, 'users/farmer_dashboard.html')

@login_required
def buyer_dashboard(request):
    return render(request, 'users/buyer_dashboard.html')

from .decorators import role_required

@login_required
@role_required('admin')
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

@login_required
@role_required('farmer')
def farmer_dashboard(request):
    return render(request, 'users/farmer_dashboard.html')

@login_required
@role_required('buyer')
def buyer_dashboard(request):
    return render(request, 'users/buyer_dashboard.html')

