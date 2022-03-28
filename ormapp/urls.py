
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('', v.home),
    path('addemp',v.add_emp),
    path('addemp2',v.add_emp2),
    path('addemp3',v.add_emp3),
    path('elist',v.emp_list),
    path('addsinger',v.addsinger),
    path('addsong',v.addsong),
    path('adduser1',v.adduser1),
    path('adduser2',v.adduser2),


]
