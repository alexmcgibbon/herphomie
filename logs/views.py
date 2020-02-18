from django.shortcuts import render

def logs_list(request):
    return render(request, 'logs/log_list.html', {})

def feeds_list(request):
    return render(request, 'logs/feeds/feed_list.html', {})
