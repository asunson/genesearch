from rest_framework import serializers
from .models import Sample
from .models import Gene

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'name')

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ('id', 'symbol', 'fpkm', 'sample')