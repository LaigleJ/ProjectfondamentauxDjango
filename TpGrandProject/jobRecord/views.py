from django.shortcuts import render
from django.db.models import Avg, Count
from jobRecord.models import JobRecord

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
