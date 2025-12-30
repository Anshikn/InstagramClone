from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import TestSerializer
from .models import Test
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# Create your views here.

# @api_view(['GET', 'POST' ])
# def test(request):
#   if request.method == 'GET':
#     queryset = Test.objects.all()
#     serializer = TestSerializer( queryset, many=True)
#     return Response(serializer.data)
#   if request.method == 'POST':
#     serializer = TestSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#     return Response(serializer.data)
#   queryset = Test.objects.all()
  
class TestView(ModelViewSet):
  queryset = Test.objects.all()
  serializer_class = TestSerializer