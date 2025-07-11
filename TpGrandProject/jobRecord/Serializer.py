from rest_framework import serializers
from jobRecord.models import JobRecord, Candidate, Industry, Skill, Contract, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'type_code', 'description', 'created_at', 'updated_at']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'created_at', 'updated_at']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name', 'created_at', 'updated_at']

class CandidateSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    industry = IndustrySerializer(read_only=True)

    class Meta:
        model = Candidate
        fields = [
            'id', 'name', 'email', 'location',
            'skills', 'industry', 'created_at', 'updated_at'
        ]

class JobRecordSerializer(serializers.ModelSerializer):
    employment_type = ContractSerializer(read_only=True)
    industry = IndustrySerializer(read_only=True)
    candidate = CandidateSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = JobRecord
        fields = [
            'id', 'work_year', 'experience_level', 'employment_type',
            'job_title', 'salary', 'salary_currency', 'salary_in_usd',
            'employee_residence', 'remote_ratio', 'company_location', 'company_size',
            'industry', 'candidate', 'category', 'created_at', 'updated_at'
        ]
