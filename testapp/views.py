from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import memberForm
from .models import members

# Create your views here.
def home(request):
    return render(request,'testapp/project.html')

#cultural page
def culturalPage(request):
    return render(request, 'testapp/cultural.html')

#technical page
def technicalPage(request):
    return render(request, 'testapp/tech.html')

#ECO page
def ecoPage(request):
    return render(request, 'testapp/eco.html')

#sport page
def sportPage(request):
    return render(request, 'testapp/sports.html')

def joinPage(request):
    if request.method=='POST':
        form  = memberForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/join')
    else:
        form = memberForm()
        

    return render(request, 'testApp/join.html', {"form": form})