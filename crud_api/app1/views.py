from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from .models import Employee
from .serializer import EmployeeSerializer
# Create your views here.

class EmployeeDetails(APIView):
    def get(self,request):
        obj= Employee.objects.all()
        serializer=EmployeeSerializer(obj,many=True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer= EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeInfo(APIView):
    def get(self,request,eid):
        try:
            obj=Employee.objects.get(eid=eid)
        except Employee.DoesNotExist:
            msg= {"msg":"Employee not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,eid):
        try:
            obj=Employee.objects.get(eid=eid)
        except Employee.DoesNotExist:
            msg= {"msg":"Employee not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,eid):
        try:
            obj=Employee.objects.get(eid=eid)
        except Employee.DoesNotExist:
            msg= {"msg":"Employee not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer=EmployeeSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,eid):
        try:
            obj=Employee.objects.get(eid=eid)
        except Employee.DoesNotExist:
            msg= {"msg":"Employee not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)