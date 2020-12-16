from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy , reverse
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
import csv , io



class Employees(ListView):
    model = Employee
    template_name = 'employee_system/list_employees.html'
    paginate_by = 20


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee_system/employee_details.html'


class CreateEmployee(SuccessMessageMixin, CreateView):
    model = Employee
    template_name = 'employee_system/employee_create.html'
    fields = ["first_name", "last_name", "employee_code", "gender", "birth_date", "email", "mobile", "hire_date",\
              "employee_type", "photo"]
    success_message = "Employee created successfully"


class UpdateEmployee(SuccessMessageMixin, UpdateView):
    model = Employee
    template_name = 'employee_system/employee_create.html'
    fields = ["first_name", "last_name", "employee_code", "gender", "birth_date", "email", "mobile", "hire_date",\
              "employee_type", "photo"]
    success_message = "Employee updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteEmployee(SuccessMessageMixin, DeleteView):
    model = Employee
    success_message = "Employee deleted successfully"
    success_url = reverse_lazy('employees:list-employees')
    template_name = 'employee_system/confirm_employee_deletion.html'


class ExportCSV(View):
    def get(self, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'
        writer = csv.writer(response)
        writer.writerow(["employee_code", "first_name", "last_name", "gender", "birth_date", "email", "mobile", "hire_date",\
              "employee_type"])
        employees = Employee.objects.all()
        for employee in employees:
            writer.writerow([employee.employee_code, employee.first_name, employee.last_name, employee.gender, employee.birth_date, employee.email, employee.mobile, employee.hire_date,\
              employee.employee_type])
        messages.info(self.request, "Data Exported Successfully")
        return response


class ImportCSV(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'employee_system/import.html')
    
    def post(self, *args, **kwargs):
        paramFile = io.TextIOWrapper(self.request.FILES['employees'].file)
        all_employees = csv.DictReader(paramFile)
        list_of_dict = list(all_employees)
        objects_list = [
        Employee(
            first_name=row['first_name'],
            last_name=row['last_name'],
            employee_code=row['employee_code'],
            gender=row['gender'],
            birth_date=row['birth_date'],
            email=row['email'],
            mobile=row['mobile'],
            hire_date=row['hire_date'],
            employee_type=row['employee_type']
                )
            for row in list_of_dict
            ]
        try:
            Employee.objects.bulk_create(objects_list)
            messages.info(self.request, "Data Imported Successfully")
        except Exception as e:
            messages.info(self.request, "Something Went Wrong")
            return HttpResponseRedirect(reverse('employees:import-csv'))
        return HttpResponseRedirect(reverse('employees:list-employees'))