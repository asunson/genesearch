from django.db import models

# Create your models here.
# add this
class Sample(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ('name',)

    def _str_(self):
        return self.name

class Gene(models.Model):
    sample = models.ManyToManyField(Sample)
    symbol = models.CharField(max_length=20)
    fpkm = models.FloatField()

    def __str__(self):
        return self.symbol

    class Meta:
        ordering = ('symbol',)