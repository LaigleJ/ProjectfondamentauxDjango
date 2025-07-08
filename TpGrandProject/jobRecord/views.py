from django.http import HttpResponse
from django.shortcuts import render

def jobRecord(request):
  context = {
        "nom": "👋 Hello Django!",
        "message": "Bienvenue dans notre première vraie page stylée ! 🎉",
    }
  return render(request, "jobRecord/jobRecord.html", context)