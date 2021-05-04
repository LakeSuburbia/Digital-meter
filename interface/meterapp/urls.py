from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views 
from .views import index, chart, UsageViewSet


router = routers.DefaultRouter()
router.register(r'usage', UsageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("restapi/", include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('chart/', chart, name='chart')
]
