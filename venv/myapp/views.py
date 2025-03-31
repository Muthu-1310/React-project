from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employee



# Create your views here.
class apple(APIView):
    def post(self,request):
        i=request.data.get('id')
        nm=request.data.get('name')
        ag=request.data.get('age')
        ma=request.data.get('mail')
        employee.objects.create(id=i,name=nm,age=ag,mail=ma)
        return Response ('saved successfully')
    
    def get(self, request):
        employees = employee.objects.all().values()  
        return Response(list(employees)) 
   
