from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Employee
from .forms import Employee_Form


# 🏠 HOME (Public)
def home(request):
    return render(request, 'front/home.html')


# 🔐 LOGIN
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'front/login.html')




# 📝 REGISTER (Optional but recommended)
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation
        if not username:
            messages.error(request, "Username is required")
            return render(request, 'front/register.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'front/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'front/register.html')

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'front/register.html')


# 🔓 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')



# 📊 DASHBOARD (Protected)
@login_required(login_url='login')
def dashboard(request):
    data = Employee.objects.all()
    form = Employee_Form()

    if request.method == 'POST':
        form = Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)  # DEBUG

    return render(request, 'front/demo.html', {
        'data': data,
        'form': form,
    })




# ✏ UPDATE
@login_required(login_url='login')
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = Employee_Form(request.POST or None, instance=employee)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'front/update.html', {'form': form})


# ❌ DELETE
@login_required(login_url='login')
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('dashboard')
