from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Task
from .serializers import TaskSerializers

# Create your views here.
@api_view(['GET'])
def index(request):
    tasks = Task.objects.all()
    serialtasks = TaskSerializers(tasks,many = True)
    return Response(serialtasks.data)


@api_view(['POST'])
def taskAdd(request):
    serialdata = TaskSerializers(data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)    

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id = pk)
    serialtask = TaskSerializers(instance = task,data = request.data)

    if serialtask.is_valid():
        serialtask.save()

    return Response(serialtask.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    tasks = Task.objects.all()
    serialtasks = TaskSerializers(tasks,many = True)
    return Response(serialtasks.data)
































    

     
