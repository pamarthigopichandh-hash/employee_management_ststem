from django.urls import path
from myapp.views import EmployeeCreateView,EmployeeUpdateView,EmployeeListView,EmployeeDetailView,EmployeeDeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employees_list'),

    path('add/',EmployeeCreateView .as_view(), name='employee_add'),

    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),

    path('<int:pk>/detail/', EmployeeDetailView.as_view(), name='employee_detail'),

    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]