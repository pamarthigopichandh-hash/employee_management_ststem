from django.contrib import admin
from.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=["EmpID","EName","ESal"]
    class meta:
        model=Employee
        fields='__all__'
