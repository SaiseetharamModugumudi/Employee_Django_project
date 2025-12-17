from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from app1.forms import Employee_Form
from app1.models import Employee


# ---------------- HOME ----------------
def home(request):
    return render(request, 'front/home.html')


# ---------------- MANUAL LOGIN ----------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Manual validation
        user = authenticate(request, username='admin', password='admin123')

        if user is not None:
            login(request, user)   # create session
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'front/login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('home')


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    data = Employee.objects.all()
    form = Employee_Form(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'front/demo.html', {
        'data': data,
        'form': form,
    })


# ---------------- UPDATE ----------------
@login_required
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = Employee_Form(request.POST or None, instance=employee)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'front/update.html', {
        'form': form,
        'employee': employee
    })


# ---------------- DELETE ----------------
@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('dashboard')
