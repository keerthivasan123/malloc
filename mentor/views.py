from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from mentee.models import startup_Details

def index(request):
    mentor = startup_Details.objects.all()
    
    context = {
    'mentor': mentor
    }
    return render(request, 'mentor/index.html',context)


def register(request):

    return render(request,'mentor/register.html')