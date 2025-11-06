import django
from django.shortcuts import redirect, render
from app1.forms import Employee_Form
from app1.models import Employee
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
    data = Employee.objects.all()
    form = Employee_Form(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'front/demo.html', {'data': data, 'form': form})





