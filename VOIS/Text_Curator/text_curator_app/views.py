from django.shortcuts import render
from subprocess import run,PIPE
import sys
# Create your views here.

def home(request):
    return render(request,'base.html')

def external(request):
    inp=request.POST.get('filename')
    out=run(sys.executable,['//Users//varadunhale//Desktop/VOIS//project.py',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'base.html',{'data1':out})
