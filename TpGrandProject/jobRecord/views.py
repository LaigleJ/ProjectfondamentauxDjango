from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import JobRecord
from .Serializer import JobRecordSerializer
from rest_framework.decorators import api_view, permission_classes

class JobRecordViewSet(viewsets.ModelViewSet):
    queryset = JobRecord.objects.all()
    serializer_class = JobRecordSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['job_title', 'employee_residence']
    ordering_fields = ['salary_in_usd', 'ordering']

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stats_view(request):
    total_jobs = JobRecord.objects.count()
    average_salary = JobRecord.objects.aggregate(Avg('salary_in_usd'))['salary_in_usd__avg']
    unique_countries = JobRecord.objects.values('company_location').distinct().count()

    context = {
        'total_jobs': total_jobs,
        'average_salary': round(average_salary, 2) if average_salary else 0,
        'unique_countries': unique_countries,
    }
    return render(request, 'jobRecord/stats.html', context)
