from django.contrib import admin
from django.urls import path
from app1.views import dashboard, update_employee, delete_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('update/<int:id>/', update_employee, name='update_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
]
