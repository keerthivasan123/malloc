from django.shortcuts import render
from django.http import HttpResponse
from mentor.models import Mentor
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from sematch.semantic.similarity import WordNetSimilarity
from . import mapMentorMentee
from .models import project_details
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

def index(request):
    mentor = Mentor.objects.all()
    
    context = {
    'mentors': mentor
    }

    return render(request, 'mentee/index.html',context)
def register(request):
    return render(request,'mentee/register.html')

def my_view(request):
    mentors = Mentor.objects.all()
    project_detailss = project_details.objects.last()
    context = {
        'mentors': mentors,
        'project_details': project_detailss

    }

    matchedMentors = []

    print("project:::")
    print(project_detailss.project_des)
    
    for mentor in mentors:
       matched = mapMentorMentee.getSimilarity(mentor,project_detailss.project_des)
       if(matched):
           matchedMentors.append(mentor)

    context = {
        'mentors': matchedMentors,
        'project_details': project_detailss

    }

    return render(request,'mentee/connected.html',context)

def project(request):
    return render(request,'mentee/projects.html')
def rate(request):
    mentors = Mentor.objects.last()
    context = {
        'mentors': mentors,

    }
    return render(request,'mentee/linked.html',context)

def rating1(request):
    mentor=Mentor.objects.all().filter(rating__gte=7)
    
    context = {
    'mentors': mentor
    }

    return render(request, 'mentee/rating.html',context)