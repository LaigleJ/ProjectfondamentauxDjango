from django.contrib import admin
from .models import JobRecord, Contract, Skill, Industry, Candidate, Category

admin.site.register(JobRecord)
admin.site.register(Contract)
admin.site.register(Skill)
admin.site.register(Industry)
admin.site.register(Candidate)
admin.site.register(Category)

