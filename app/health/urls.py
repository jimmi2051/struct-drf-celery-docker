from health.views import healthCheck, testCelery, testS3Config
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('healthCheck', healthCheck, name="healthCheck"),
    path('testCelery', testCelery, name="testCelery"),
    path('testS3Config', testS3Config, name="testS3Config")
]
