from django.urls import path
from .views import feedback_list, feedback_detail, feedback_add, job_list, feedbacks_for_job_title, feedbacks_grouped_by_job_title, feedbacks_for_job

urlpatterns = [
    path('', feedback_list, name='feedback_list'),  # liste tous les feedbacks
    path('add/', feedback_add, name='feedback_add'),
    path('<int:pk>/', feedback_detail, name='feedback_detail'),  # détail d’un feedback
    path('jobs/', job_list, name='job_list'),
    path('jobs/<str:job_title>/', feedbacks_for_job_title, name='feedbacks_for_job_title'),
    path('feedbacks/by-job/', feedbacks_grouped_by_job_title, name='feedbacks_grouped_by_job'),
    path('feedback/jobs/<str:title>/', feedbacks_for_job, name='feedbacks_for_job'),

]
