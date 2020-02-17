from django.conf import settings
from django.db import models
from django.utils import timezone

class WeighIn(models.Model):
	animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	weight = models.PositiveSmallIntegerField(blank=True, null=True)

	def __str__(self):
		return self.animal.name

class Shed(models.Model):
	animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	success = models.BooleanField()

class Feed(models.Model):

	PINKY = 'PI'
	TWOPINKY = 'TP'
	SMALLFUZZY = 'SF'
	REGULARFUZZY = 'RF'
	HOPPER = 'HO'
	SMALLADULT = 'SA'
	REGULARADULT = 'RA'
	LARGEADULT = 'LA'
	
	FEED_CHOICES = [
        (PINKY, 'Pinky'),
        (TWOPINKY, 'Two Pinkies'),
        (SMALLFUZZY, 'Small Fuzzy'),
        (REGULARFUZZY, 'Regular Fuzzy'),
        (HOPPER, 'Hopper'),
        (SMALLADULT, 'Small Adult'),
        (REGULARADULT, 'Regular Adult'),
        (LARGEADULT, 'Large Adult')
    ]

	animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	feed = models.CharField(
        max_length=2,
        choices=FEED_CHOICES,
        default=PINKY,
    )
	feed_weight = models.PositiveSmallIntegerField(blank=True, null=True)
	success = models.BooleanField()

class Measurement(models.Model):
	animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	measurement = models.PositiveSmallIntegerField(blank=True, null=True)

class DailyCheck(models.Model):
	animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	water_changed = models.BooleanField()
	animal_seen = models.BooleanField()
	temperature_measured = models.PositiveSmallIntegerField(blank=True, null=True)