from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/main')
    else:
        return render(request,'login_reg_app/index.html')

def results(request):
    return render(request, 'farmers/results.html')

def show_fMarket(request):
    return render(request, 'farmers/index.html')
