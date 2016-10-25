from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/main')
    else:
        return render(request,'login_reg_app/index.html')

def results(request):
<<<<<<< HEAD
    return render(request, 'farmers/results.html')

def show_fMarket(request):
    return render(request, 'farmers/index.html')
=======
    if request.method == 'POST':
        return render(request, 'farmers/results.html')
>>>>>>> 146fd5965a83c3e0c64ed5f2be3265633cd7d25d
