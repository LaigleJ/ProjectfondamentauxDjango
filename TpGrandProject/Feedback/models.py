from django.db import models
from jobRecord.models import JobRecord, Candidate  # Assure-toi que ces modèles existent bien dans jobRecord

class Feedback(models.Model):
    job = models.ForeignKey(JobRecord, on_delete=models.CASCADE, related_name='feedbacks')
    author = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True, related_name='feedbacks')
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Feedback by {self.author} on {self.job}"
