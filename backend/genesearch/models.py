from django.db import models

# Create your models here.
# add this
class Sample(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def _str_(self):
        return self.name

class Gene(models.Model):
    symbol = models.CharField(max_length=20)
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
        ordering = ('symbol',)