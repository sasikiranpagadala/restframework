"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from quickstart import views

# using view sets
from django.db import router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('',views.Studentviewset,basename='student')
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quickstart.urls')),

    # using view sets
    path('api4/',include(router.urls)),
    
]
