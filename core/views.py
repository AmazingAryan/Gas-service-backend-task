from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerRegistrationForm, StaffRegistrationForm, ServiceRequestForm
from .models import User, ServiceRequest

def home(request):
    return render(request, 'core/home.html')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'customer'
            user.save()
            return redirect('customer_login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'core/register_customer.html', {'form': form, 'user_type': 'Customer'})

def register_staff(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'staff'
            user.save()
            return redirect('staff_login')
    else:
        form = StaffRegistrationForm()
    return render(request, 'core/register_staff.html', {'form': form, 'user_type': 'Staff'})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             if user.user_type == 'customer':
#                 return redirect('customer_dashboard')
#             elif user.user_type == 'staff':
#                 return redirect('staff_dashboard')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'core/login.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == 'customer':
                login(request, user)
                return redirect('customer_dashboard')
            else:
                form.add_error(None, 'You are not authorized as a customer.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/customer_login.html', {'form': form})


def staff_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.user_type == 'staff':
                login(request, user)
                return redirect('staff_dashboard')
            else:
                form.add_error(None, 'You are not authorized as staff.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/staff_login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def customer_dashboard(request):
    return render(request, 'core/customer_dashboard.html', {'user': request.user})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'core/submit_request.html', {'form': form})

@login_required
def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'core/track_request.html', {'requests': requests})

@login_required
def staff_dashboard(request):
    requests = ServiceRequest.objects.filter(customer__city=request.user.city)
    return render(request, 'core/staff_dashboard.html', {'requests': requests})

@login_required
def update_status(request, service_id):
    service_request = ServiceRequest.objects.get(service_id=service_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(ServiceRequest.STATUS_TYPES).keys():
            service_request.status = status
            service_request.save()
            return redirect('staff_dashboard')
    return render(request, 'core/update_status.html', {'service_request': service_request})
