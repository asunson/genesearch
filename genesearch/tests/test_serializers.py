from rest_framework import serializers
from ..models import Gene, Sample
from django.test import TestCase
from ..serializers import GeneSerializer, SampleSerializer
class SerializerTestCase(TestCase):
    def setUp(self):
        self.sample = Sample(name = "Sample 1", species = "Human", status = "Vitro")
        self.sample.save()

        self.gene = Gene(symbol = 'GENE1', fpkm = 1.1, sample = self.sample)
        self.gene.save()

        self.sampleSerializer = SampleSerializer(instance = self.sample)
        self.geneSerializer = GeneSerializer(instance = self.gene)  

    def test_sample_serializer_works(self):
        sample_data = self.sampleSerializer.data
        self.assertEqual(
            set(sample_data.keys()), 
            set(['id', 'name', 'species', 'status'])
        )
        self.assertEqual(
            set(sample_data.values()), 
            set([1, "Sample 1", "Human", "Vitro"])
        )

    def test_gene_serializer_works(self):
        gene_data = self.geneSerializer.data
        self.assertEqual(
            set(gene_data.keys()), 
            set(['id', 'symbol', 'fpkm', 'sample_name'])
        )
        self.assertEqual(
            set(gene_data.values()),
            set([1, 'GENE1', 1.1, 'Sample 1'])
        )