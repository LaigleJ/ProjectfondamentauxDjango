from django.urls import path
from .views import average_ratings, feedback_add, feedbacks_for_job_title, job_titles_list
from rest_framework.routers import DefaultRouter
from .views import FeedbackViewSet

router = DefaultRouter()
router.register(r'feedback', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', job_titles_list, name='job_titles_list'),
    path('jobs/<str:job_title>/', feedbacks_for_job_title, name='feedbacks_for_job_title'),
    path('add/', feedback_add, name='feedback_add'),
     path('averages/', average_ratings, name='average_ratings'),
] + router.urls
