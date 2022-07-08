# Third Party
from django.urls import path
from health.views import healthCheck
from health.views import testCelery
from health.views import testS3Config

urlpatterns = [
    path('healthCheck', healthCheck, name="healthCheck"),
    path('testCelery', testCelery, name="testCelery"),
    path('testS3Config', testS3Config, name="testS3Config"),
]
