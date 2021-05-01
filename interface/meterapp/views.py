from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Hello, world.")


class UsageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usage.objects.all().order_by('-timestamp')
    serializer_class = UsageSerializer
    #permission_classes = [permissions.IsAuthenticated]

#class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
#    queryset = Data.objects.all().order_by('-updatetime')
#    serializer_class = DataSerializer
    #permission_classes = [permissions.IsAuthenticated]