from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse, JsonResponse
#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from decoderapp.models import DeviceList
from decoderapp.serializers import DeviceListSerializer
#from django.views.decorators.csrf import csrf_exempt

"""
tutorial 3
"""

class decoder_list(APIView):
    def get(self, rquest, format=None):
        dev = DeviceList.objects.all()
        serializer = DeviceListSerializer(dev, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class decoder_detail(APIView):
    def get_object(self,pk):
       try:
           dev = DeviceList.objects.get(id=pk)
       except DeviceList.DoesNotExist:
           raise Http404
       return dev
    
    def get(self, request, pk, format=None):    
        dev = self.get_object(pk)
        serializer = DeviceListSerializer(dev)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        dev = self.get_object(pk)
        serializer = DeviceListSerializer(dev, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):    
        dev = self.get_object(pk)
        dev.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
        

"""
tutorial 2


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