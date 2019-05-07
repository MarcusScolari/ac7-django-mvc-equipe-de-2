from django.shortcuts import render

# Create your views here.
def ads(request):
    return render(request, 'ads.html')

def bd(request):
    return render(request, 'bd.html')

def si(request):
    return render(request, 'si.html')

def gti(request):
    return render(request, 'gti.html')