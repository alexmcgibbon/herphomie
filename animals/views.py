from django.shortcuts import render
from django.utils import timezone
from .models import Animal

def animal_list(request):
	animals = Animal.objects.order_by('name')
	return render(request, 'animals/animal_index.html', {'animals': animals})
