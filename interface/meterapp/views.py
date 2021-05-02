from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import date, timedelta, datetime
from .models import *
from .serializers import *


class UsageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows usages to be viewed or edited.
    """
    queryset = Usage.objects.all().order_by('-timestamp')
    serializer_class = UsageSerializer
    #permission_classes = [permissions.IsAuthenticated]

 
def chart(request):
    labels = []
    data = get_hourly_usage(request)
    for i in range(24):
        labels.append(str(i)+"   - ")
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
#Get the hourly usage today
def get_hourly_usage(request):
    day = date.today()
    allEntriesToday = Usage.objects.filter(timestamp__date = day).order_by('-timestamp')
    hourlyUsage = [0] * 24
    for i in range(24):
        allEntriesHour = allEntriesToday.filter(timestamp__hour = i).order_by('-timestamp')
        if allEntriesHour.count() >= 2:
            hourlyUsage[i] = allEntriesHour.first().nighttime - allEntriesHour.last().nighttime 
        

    return hourlyUsage


def index(request):
    return render(request, 'index.html')

        
    