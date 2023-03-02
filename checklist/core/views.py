from django.shortcuts import render
from .serializers import TaskSerializer
from . models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def HomeView(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def DetailView(request, id):
    tasks = Task.objects.get(id =id)
    serializer = TaskSerializer(tasks, many =False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateView(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def UpdateView(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(data = request.data, instance= tasks)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def DeleteView(request,id):
    tasks =Task.objects.get(id = id)
    tasks.delete()
    return Response({'msg':'Data deleted'})



# Create your views here.
