from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'farmers/index.html')

def results(request):
    if request.method == 'POST':
        return render(request, 'farmers/results.html')
