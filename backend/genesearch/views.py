from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SampleSerializer, GeneSerializer, GeneSearchSerializer
from .models import Sample, Gene

class SampleView(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class GeneView(viewsets.ModelViewSet):
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()

# class GeneSearchView(viewsets.ModelViewSet):
#     serializer_class = GeneSearchSerializer
