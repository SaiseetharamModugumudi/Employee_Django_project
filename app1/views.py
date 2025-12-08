from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app1.forms import Employee_Form
from app1.models import Employee


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


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('dashboard')
