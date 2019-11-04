from rest_framework import serializers
from .models import Sample
from .models import Gene

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'name', 'species', 'status')

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ('id', 'symbol', 'fpkm', 'sample')

class GeneSearchSerializer(serializers.ModelSerializer):
    sample_name = serializers.CharField(source='sample.name')

    class Meta:
        model = Gene
        fields = ('symbol', 'fpkm', 'sample_name')
