from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'usage', views.UsageViewSet)
#router.register(r'data', views.UsageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("restapi/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chart/', views.chart, name='chart')
    #path('starter/', views.starter, name='starter'),
]
