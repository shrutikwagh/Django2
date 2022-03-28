
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('addimage', v.addimage),
    path('msg', v.msg_data),


]
