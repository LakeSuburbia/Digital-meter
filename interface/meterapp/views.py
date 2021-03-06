from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import date, timedelta, datetime, timezone
from .models import *
from .serializers import *


class UsageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows usages to be viewed or edited.
    """
    queryset = Usage.objects.all().order_by('-timestamp')
    serializer_class = UsageSerializer

 
def chart(request):
    """
    Function that provides the usage data in JSON format to the chart.js module
    """
    labels = []
    data = get_usage_data(request)
    for i in range(24):
        labels.append(str(i)+"h00")
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
def get_usage_data(request):
    """
    Function that gathers all the usage data of today and calculates the hourly usage
    """
    day = date.today()
    allEntriesToday = Usage.objects.filter(timestamp__date = day).order_by('-timestamp')
    hourlyUsage = [0] * 24
    totalUsage = 0
    for i in range(24):
        allEntriesHour = allEntriesToday.filter(timestamp__hour = i).order_by('-timestamp')
        if allEntriesHour.count() >= 2:

            # The hourly usage is calculated by subtracting the newest data by the oldest data of this particular hour.
            # This isn't 100% accurate since we're missing data the last / first minute of every hour

            nighttime = allEntriesHour.first().nighttime - allEntriesHour.last().nighttime
            daytime = allEntriesHour.first().daytime - allEntriesHour.last().daytime

            # For now, I'll add the nighttime and daytime usage
            # In the future I'll be able to interpret these seperately
            hourlyUsage[i] = round(nighttime + daytime, 5)

    return hourlyUsage


def index(request):
    """
    Function that renders the index page and calculates the total and average hourly usage
    """

    totalUsage = 0

    for data in get_usage_data(request):
        totalUsage += data 

    # Time in hours (expressed as decimals, to calculate the averageUsage)
    now = datetime.now()+timedelta(hours=2)
    time = now.hour + now.minute/60 + now.second/3600

    return render(request, 'index.html', {
        'totalUsage': round(totalUsage,5),
        'averageUsage': round(totalUsage/time,5)
    })

        
    