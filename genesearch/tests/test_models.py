from django.test import TestCase, Client
from ..models import Sample, Gene

class SampleGeneTestCase(TestCase):
    def setUp(self):
        s1 = Sample(name = "Sample 1", species = "Human", status = "Vitro")
        s1.save()
        s2 = Sample(name = "Sample 2", species = "Human", status = "Vivo")
        s2.save()
        s3 = Sample(name = "Sample 3", species = "Mouse", status = "Vivo")
        s3.save()

        g1_1 = Gene.objects.create(symbol = 'GENE1', fpkm = 1.1, sample = s1)
        g1_1.save()
        g1_2 = Gene.objects.create(symbol = 'GENE1', fpkm = 1.2, sample = s2)
        g1_2.save()
        g1_3 = Gene.objects.create(symbol = 'GENE1', fpkm = 1.3, sample = s3)
        g1_3.save()

        g2_1 = Gene.objects.create(symbol = 'GENE2', fpkm = 2.1, sample = s1)
        g2_1.save()
        g2_2 = Gene.objects.create(symbol = 'GENE2', fpkm = 2.2, sample = s2)
        g2_2.save()

        g3_1 = Gene.objects.create(symbol = 'GENE3', fpkm = 3.0, sample = s1)
        g3_1.save()

    def test_samples_have_species(self):
        sample_1 = Sample.objects.get(name="Sample 1")
        sample_2 = Sample.objects.get(name="Sample 2")
        sample_3 = Sample.objects.get(name="Sample 3")

        self.assertEqual(sample_1.species, "Human")
        self.assertEqual(sample_2.species, "Human")
        self.assertEqual(sample_3.species, "Mouse")

    def test_samples_have_status(self):
        sample_1 = Sample.objects.get(name="Sample 1")
        sample_2 = Sample.objects.get(name="Sample 2")
        sample_3 = Sample.objects.get(name="Sample 3")

        self.assertEqual(sample_1.status, "Vitro")
        self.assertEqual(sample_2.status, "Vivo")
        self.assertEqual(sample_3.status, "Vivo")

    def test_samples_were_stored_properly(self):
        self.assertEqual(Sample.objects.count(), 3)

    def test_sample1_should_have_3_genes(self):
        sample_1 = Sample.objects.get(name="Sample 1")
        sample_1_genes = sample_1.genes

        self.assertEqual(sample_1_genes.count(), 3)

        # sample 1 should have these specific genes
        gene_names = ['GENE1', 'GENE2', 'GENE3']
        genes = sample_1_genes.all()
        for i in range(sample_1_genes.count()):
            self.assertEqual(genes[i].symbol, gene_names[i])
        
    def test_sample3_should_only_have_1_gene(self):
        sample_3 = Sample.objects.get(name="Sample 3")
        sample_3_genes = sample_3.genes
        self.assertEqual(sample_3_genes.count(), 1)