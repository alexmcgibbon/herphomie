from django.shortcuts import render
from django.utils import timezone
from .models import Feed

def logs_list(request):
    return render(request, 'logs/log_list.html', {})

def feeds_list(request):
	feeds = Feed.objects.order_by('date')
	return render(request, 'logs/feeds/feed_list.html', {'feeds': feeds})
