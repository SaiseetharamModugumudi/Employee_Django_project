from django.contrib import admin
from django.urls import path
from app1.views import (
    home, dashboard,
    update_employee, delete_employee,
    login_view, logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('login/', login_view, name='login'),     # manual login
    path('logout/', logout_view, name='logout'),  # manual logout

    path('dashboard/', dashboard, name='dashboard'),
    path('update/<int:id>/', update_employee, name='update_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
]
