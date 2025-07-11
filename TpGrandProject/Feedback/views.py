from django.shortcuts import render, redirect
from django.db.models import Avg
from rest_framework import viewsets
from .models import Feedback, JobRecord
from .Serializer import FeedbackSerializer
from .forms import FeedbackForm


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

def feedback_add(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_titles_list')  # ou liste des feedbacks
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_add.html', {'form': form})

def job_titles_list(request):
    # On récupère les titres uniques (sans doublons)
    titles = JobRecord.objects.values_list('job_title', flat=True).distinct()
    return render(request, 'feedback/job_titles_list.html', {'titles': titles})

def feedbacks_for_job_title(request, job_title):
    rating_filter = request.GET.get('rating')  # récupère la note depuis l'URL (ex: ?rating=4)
    
    feedbacks = Feedback.objects.filter(job__job_title=job_title)
    
    if rating_filter:
        feedbacks = feedbacks.filter(rating=rating_filter)
    
    context = {
        'job_title': job_title,
        'feedbacks': feedbacks,
        'rating_filter': rating_filter,
    }
    return render(request, 'feedback/feedbacks_for_job_title.html', context)

def average_ratings(request):
    # On récupère les jobs avec la moyenne des notes de leurs feedbacks
    jobs_with_avg = JobRecord.objects.annotate(avg_rating=Avg('feedbacks__rating'))

    return render(request, 'feedback/average_ratings.html', {
        'jobs_with_avg': jobs_with_avg
    })