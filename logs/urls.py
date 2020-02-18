from django.urls import path
from . import views

urlpatterns = [
    path('', views.logs_list, name='log_list'),
    path('feeds/', views.feeds_list, name='feed_list'),
]