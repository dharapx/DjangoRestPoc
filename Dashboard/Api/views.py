from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from .models import Department, Employees
from .serializers import DepartmentSerializer, EmployeesSerializer


# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def department_api(request, dep_id=0):
    if request.method == 'GET':
        if dep_id > 0:
            try:
                department = Department.objects.get(DepartmentId=dep_id)
                departments_serializer = DepartmentSerializer(department, many=False)
            except Department.DoesNotExist:
                # return JsonResponse({})
                return Response({}, status=status.HTTP_200_OK)
        else:
            departments = Department.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
        # return JsonResponse(departments_serializer.data, safe=False)
        return Response(departments_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # print(request.data)
        # department_data = JSONParser().parse(request)
        # print(department_data)
        departments_serializer = DepartmentSerializer(data=request.data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            # return JsonResponse("Department Added Successfully", safe=False)
            return Response("Department Added Successfully", status=status.HTTP_201_CREATED)
        # return JsonResponse("Invalid Data set", safe=False)
        return Response("Invalid Data set", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentId=department_data.get('DepartmentId'))
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
        #     return JsonResponse(f"Update Successfully", safe=False)
        # return JsonResponse(f"Failed To Update", safe=False)
            return Response(f"Update Successfully", status=status.HTTP_200_OK)
        return Response(f"Failed To Update", status=status.HTTP_304_NOT_MODIFIED)

    elif request.method == "DELETE":
        department = Department.objects.get(DepartmentId=dep_id)
        department.delete()
        # return JsonResponse("Delete Successful", safe=False)
        return Response("Delete Successful", status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_api(request, emp_id=0):
    if request.method == 'GET':
        if emp_id > 0:
            try:
                employee = Employees.objects.get(EmployeeId=emp_id)
                employees_serializer = EmployeesSerializer(employee, many=False)
                data = employees_serializer.data
            except Employees.DoesNotExist:
                data = {}
        else:
            employees = Employees.objects.all()
            employees_serializer = EmployeesSerializer(employees, many=True)
            data = employees_serializer.data
        # return JsonResponse(data, safe=False)
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # employee_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=request.data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            # return JsonResponse("Employee Added Successfully", safe=False)
            return Response("Employee Added Successfully", status=status.HTTP_201_CREATED)
        # return JsonResponse("Invalid Data set", safe=False)
        return Response("Invalid Data set", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data.get('EmployeeId'))
        employee_serializer = EmployeesSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response(f"Update Successfully", status=status.HTTP_200_OK)
        return Response(f"Failed To Update", status=status.HTTP_304_NOT_MODIFIED)
    elif request.method == "DELETE":
        department = Department.objects.get(EmployeeId=emp_id)
        department.delete()
        return Response("Delete Successful", status=status.HTTP_200_OK)
