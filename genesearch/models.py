from django.db import models

# Create your models here.
# add this
class Sample(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        ordering = ('name', 'species', 'status')

    def _str_(self):
        return self.name

class Gene(models.Model):
    symbol = models.CharField(max_length=50)
    fpkm = models.FloatField()
    sample = models.ForeignKey(
        Sample, 
        on_delete=models.CASCADE, 
        related_name='genes', 
        null=True
    )

    def __str__(self):
        return self.symbol

    class Meta:
        ordering = ('symbol', 'sample', 'fpkm')