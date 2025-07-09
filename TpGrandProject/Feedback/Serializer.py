from rest_framework import serializers
from .models import Feedback
from jobRecord.Serializer import JobRecordSerializer, CandidateSerializer
class FeedbackSerializer(serializers.ModelSerializer):
    job = JobRecordSerializer(read_only=True)
    author = CandidateSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'job', 'rating', 'comment', 'created_at', 'updated_at']
    
    def validate_rating(self, value):
        if value is None or not (1 <= value <= 5):
            raise serializers.ValidationError("La note doit être comprise entre 1 et 5.")
        return value