from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
#from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

# using api view
@api_view(['GET'])
def home(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student,many=True)
    return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update_student(request,id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(instance=student,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response('student got deleted')

#using generic views and mixins
class Studentlist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)

class Studentcreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request):
        return self.create(request)

class Studentdis(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)

class Studentup(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

class Studentdel(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)

#updated version usage of generic views and mixins

class Studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class Studentrud(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)

    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)


# using Concrete generic view classes

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# using view sets

class Studentviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]