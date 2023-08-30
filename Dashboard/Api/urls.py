from django.urls import path
from . import views

urlpatterns = [
    path(r'department/', views.department_api),
    path(r'department/<int:dep_id>', views.department_api),
    path(r'employee/', views.employee_api),
    path(r'employee/<int:dep_id>', views.employee_api),
]
