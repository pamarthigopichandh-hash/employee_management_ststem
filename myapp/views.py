from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView,DeleteView

from myapp.models import Employee
from django.urls import reverse_lazy



# 1 Create your views here.
class EmployeeCreateView(CreateView):
    model=Employee
    fields='__all__'
    template_name='myapp/employee_form1.html'
    success_url= reverse_lazy('employees_list')

#---2---------------Employee Update View--------------------
class EmployeeUpdateView(UpdateView):
    model=Employee
    fields='__all__'
    template_name='myapp/employee_form2.html'
    success_url= reverse_lazy('employees_list')

#-----3-------------Employee List View--------------------
class EmployeeListView(ListView):
    model=Employee
    template_name='myapp/employee_list.html'
    context_object_name='employees'


#-----4-------------Employee Detail View--------------------
class EmployeeDetailView(DetailView):
    model=Employee
    template_name='myapp/employee_detail.html'
    context_object_name='employee'


#-----5-------------Employee Delete View--------------------
class EmployeeDeleteView(DeleteView):
    model =Employee
    template_name='myapp/employee_confirm_delete.html'
    success_url= reverse_lazy('employees_list')