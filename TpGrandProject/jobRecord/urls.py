from django.urls import path
from .views import stats_view
from rest_framework.routers import DefaultRouter
from jobRecord.views import JobRecordViewSet

router = DefaultRouter()
router.register(r'jobrecords', JobRecordViewSet, basename='jobrecord')

urlpatterns = [
    path('', stats_view, name='stats_view'),
] + router.urls 