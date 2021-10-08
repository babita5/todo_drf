from django.contrib import admin
from django.utils import path

app_name = 'api'

urlpatterns = [
    path('',views.APIView.as_view(), name = 'api_view'),
    ]