from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm
from jobRecord.models import JobRecord

def feedback_add(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_add.html', {'form': form})

def feedback_list(request):
    min_rating = request.GET.get('min_rating')
    feedbacks = Feedback.objects.select_related('job').all()
    if min_rating is not None:
        try:
            min_rating = int(min_rating)
            feedbacks = feedbacks.filter(rating__gte=min_rating)
        except ValueError:
            pass
    context = {
        'feedbacks': feedbacks.order_by('-created_at'),
        'min_rating': min_rating or '',
    }
    return render(request, 'feedback/feedback_list.html', context)

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})

def job_list(request):
    # Récupérer les titres distincts
    job_titles = JobRecord.objects.values_list('job_title', flat=True).distinct().order_by('job_title')
    
    selected_title = request.GET.get('job_title')
    feedbacks = None
    if selected_title:
        feedbacks = Feedback.objects.select_related('job').filter(job__job_title=selected_title).order_by('-created_at')

    context = {
        'job_titles': job_titles,
        'selected_title': selected_title,
        'feedbacks': feedbacks,
    }
    return render(request, 'feedback/job_list.html', context)

def feedbacks_for_job_title(request, job_title):
    feedbacks = Feedback.objects.filter(job__job_title=job_title).order_by('-created_at')
    return render(request, 'feedback/feedbacks_for_job.html', {'feedbacks': feedbacks, 'job_title': job_title})

def feedbacks_grouped_by_job_title(request):
    # Récupérer tous les jobs
    jobs = JobRecord.objects.all()
    # Pour chaque job, on peut accéder aux feedbacks via la relation inverse si elle existe, sinon on filtre
    # Par exemple, si Feedback a un ForeignKey vers Job nommé "job", on peut faire job.feedback_set.all()

    # Passer la liste des jobs (avec leurs feedbacks) au template
    return render(request, 'feedback/feedbacks_grouped_by_job.html', {'jobs': jobs})

def feedbacks_for_job(request, job_name):
    feedbacks = Feedback.objects.filter(job__job_title=job_name).order_by('-created_at')
    return render(request, 'feedback/feedbacks_for_job.html', {'feedbacks': feedbacks, 'job_name': job_name})
