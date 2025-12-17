from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app1.forms import Employee_Form
from app1.models import Employee


def home(request):
    return render(request, 'front/home.html')


@login_required
def dashboard(request):
    data = Employee.objects.all()
    form = Employee_Form(request.POST or None)

    # CREATE - handle form submission
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'front/demo.html', context)


@login_required
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = Employee_Form(request.POST or None, instance=employee)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'employee': employee
    }
    return render(request, 'front/update.html', context)


@login_required
def delete_employee(request, id):
    if request.method == 'POST' or request.method == 'GET':
        # NOTE: It's safer to delete via POST; current UI may use GET links.
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
    return redirect('dashboard')


@login_required
def delete_list(request):
    """Render a page listing employees with delete links (requires login)."""
    data = Employee.objects.all()
    return render(request, 'front/del.html', {'data': data})