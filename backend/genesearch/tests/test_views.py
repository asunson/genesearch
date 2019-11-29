from django.test import TestCase, Client
from ..models import Sample, Gene

class APITestCase(TestCase):
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

    def test_get_genes_should_return_a_list_of_all_genes(self):
        genes = [
            {
                "id": 1,
                "symbol": "GENE1",
                "fpkm": 1.1,
                "sample": 1
            },
            {
                "id": 2,
                "symbol": "GENE1",
                "fpkm": 1.2,
                "sample": 2
            },
            {
                "id": 3,
                "symbol": "GENE1",
                "fpkm": 1.3,
                "sample": 3
            },
            {
                "id": 4,
                "symbol": "GENE2",
                "fpkm": 2.1,
                "sample": 1
            },
            {
                "id": 5,
                "symbol": "GENE2",
                "fpkm": 2.2,
                "sample": 2
            },
            {
                "id": 6,
                "symbol": "GENE3",
                "fpkm": 3.0,
                "sample": 1
            }
        ]

        c = Client()

        response = c.get('/api/genes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), genes)

    def test_get_samples_should_return_a_list_of_all_samples(self):
        samples = [
            {
                'id': 1, 
                'name': 'Sample 1',
                'species': 'Human',
                'status': 'Vitro'
            },
            {
                'id': 2, 
                'name': 'Sample 2',
                'species': 'Human',
                'status': 'Vivo'
            },
            {
                'id': 3, 
                'name': 'Sample 3',
                'species': 'Mouse',
                'status': 'Vivo'
            }
        ]

        c = Client()
        response = c.get('/api/samples/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), samples)
    
    def test_post_request_returns_genes_of_interest(self):
        genes = [
            {
                "id": 1,
                "symbol": "GENE1",
                "fpkm": 1.1,
                "sample": 1
            },
            {
                "id": 2,
                "symbol": "GENE1",
                "fpkm": 1.2,
                "sample": 2
            },
            {
                "id": 3,
                "symbol": "GENE1",
                "fpkm": 1.3,
                "sample": 3
            },
            {
                "id": 4,
                "symbol": "GENE2",
                "fpkm": 2.1,
                "sample": 1
            },
            {
                "id": 5,
                "symbol": "GENE2",
                "fpkm": 2.2,
                "sample": 2
            }
        ]

        c = Client()
        response = c.post('/api/search/', {"geneList": ['GENE1', 'GENE2']})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), genes)