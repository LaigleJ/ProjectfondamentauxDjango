from django.urls import path
from .views import jobRecord

urlpatterns = [
    path('', jobRecord),
]