from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.views  import APIView
from restapp.models import Employee
from restapp.serializer import EmployeeSerilalizer
from rest_framework.response import Response
# Create your views here.
class APICRUDview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        serializer=EmployeeSerilalizer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs): 
        serializer=EmployeeSerilalizer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            no=serializer.data.get('no')
            role=serializer.data.get('role')
            salary=serializer.data.get('salary')
            location=serializer.data.get('location')
            name='{}'.format(name)
            no='{}'.format(no)
            role='{}'.format(role)
            salary='{}'.format(salary)
            location='{}'.format(location)
            return Response({'name':name,'no':no,'role':role,'salary':salary,'location':location})
        else:
            return Response(serializer.errors,status=400)
    def put(self,request):
        return Response('These Response is from the put method')
    def patch(self,request):
        return Response('These response from the patch method')
    def delete(self,response):
        return Response('These response is from the delete method')
    
