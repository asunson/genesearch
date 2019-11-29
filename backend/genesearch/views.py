from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SampleSerializer, GeneSerializer
from .models import Sample, Gene

class SampleView(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()

class GeneView(viewsets.ModelViewSet):
    serializer_class = GeneSerializer
    queryset = Gene.objects.all()

@api_view(['POST'])
def getGeneInformation(request):
    queryset = Gene.objects.filter(symbol__in=request.data["geneList"])
    data = GeneSerializer(queryset, many=True).data
    return Response(data)