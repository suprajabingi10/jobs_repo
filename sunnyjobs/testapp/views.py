from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

from testapp.models import HydJobs
from testapp.models import BngJobs
from testapp.models import PuneJobs
def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)
def bngjobs_view(request):
    jobs_list=BngJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/bngjobs.html',my_dict)
def punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)
