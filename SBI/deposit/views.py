from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DeposteApplicationForm

# Create your views here.
@login_required
def show_deposit(request):
    form = DeposteApplicationForm()
    if request.method=='POST':
        form = DeposteApplicationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
    return render(request,'deposit/deposit.html',{'form':form})

def thanks(request):

    return render(request,'deposit/response.html', {'name':'name'})

def index(request):
    return render(request,'loan/index.html')

