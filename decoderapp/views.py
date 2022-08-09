from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decoderapp.models import DeviceList
from decoderapp.serializers import DeviceListSerializer
from django.views.decorators.csrf import csrf_exempt

"""
tutorial 2
"""

@api_view(['GET','POST'])
def decoder_list(request):
    if request.method == 'GET':
        dev = DeviceList.objects.all()
        serializer = DeviceListSerializer(dev, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeviceListSerializer(data=data)
        if serializer.is_valid():
            seralizer.save()
            return Response(seralizer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def decoder_detail(request, pk):
    try:
        dev = DeviceList.objects.get(pk=pk)
    except DeviceList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = DeviceListSerializer(dev)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DiviceListSerializer(dev, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        dev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
tutorial 1
@csrf_exempt
def decoder_list(request):
    if request.method == 'GET':
        dev = DeviceList.objects.all()
        serializer = DeviceListSerializer(dev, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeviceListSerializer(data=data)
        if serializer.is_valid():
            seralizer.save()
            return JsonResponse(seralizer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def decoder_detail(request, pk):
    try:
        dev = DeviceList.objects.get(pk=pk)
    except DeviceList.DoesNotExist:
        return HttpResponse(status=404)
        
    if request.method == 'GET':
        serializer = DeviceListSerializer(dev)
        return JsonResponse(serializer.data)
        
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DiviceListSerializer(dev, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        
    elif request.method == 'DELETE':
        dev.delete()
        return HttpResponse(status=204)
"""

# Create your views here.
def decoder(request):
    return HttpResponse("Testing page")