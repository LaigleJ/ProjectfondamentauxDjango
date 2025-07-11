from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobRecordViewSet, stats_view
from jobRecord.views import stats_view
from jobRecord.views import JobRecordViewSet

router = DefaultRouter()
router.register(r'jobrecords', JobRecordViewSet, basename='jobrecord')

urlpatterns = [
    path('stats/', stats_view, name='stats_view'),
] + router.urls 