from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('add/',post_student),
    path('update/<int:id>/',update_student),
    path('delete/<int:id>/',delete_student),

    # using generic views and mixins
    path('api/',Studentlist.as_view()),
    path('api/add/',Studentcreate.as_view()),
    path('api/get/<int:pk>/',Studentdis.as_view()),
    path('api/up/<int:pk>/',Studentup.as_view()),
    path('api/del/<int:pk>/',Studentdel.as_view()),

    path('api2/',Studentlistcreate.as_view()),
    path('api2/rud/<int:pk>/',Studentrud.as_view()),

    # using Concrete generic view classes
    path('api3/',StudentListCreate.as_view()),
    path('api3/rud/<int:pk>/',StudentRetriveUpdateDelete.as_view()),

]