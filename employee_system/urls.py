from django.conf.urls import url
from . import views


app_name = 'employees'

urlpatterns = [
    url(r'^$', views.Employees.as_view() , name='list-employees'),
    url(r'^create', views.CreateEmployee.as_view(), name='create-employee'),
    url(r'^show/(?P<pk>\d+)/$', views.EmployeeDetail.as_view(), name='show-employee'),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateEmployee.as_view(), name='update-employee'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteEmployee.as_view(), name='delete-employee'),
    url(r'^export/csv/$' , views.ExportCSV.as_view(), name='export-csv'),
    url(r'^import/csv/$' , views.ImportCSV.as_view(), name='import-csv'),
]