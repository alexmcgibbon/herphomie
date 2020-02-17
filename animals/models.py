from django.conf import settings
from django.db import models
from django.utils import timezone

class Species(models.Model):
	species = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Species'

	def __str__(self):
		return self.species

class Animal(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_acquired = models.DateField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return self.name