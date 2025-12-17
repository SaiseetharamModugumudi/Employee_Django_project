from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app1.views import home, dashboard, update_employee, delete_employee, delete_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update/<int:id>/', update_employee, name='update_employee'),
    path('delete/<int:id>/', delete_employee, name='delete_employee'),
    path('delete-list/', delete_list, name='delete_list'),
    path('login/', auth_views.LoginView.as_view(template_name='front/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
