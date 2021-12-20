from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreditApplicationForm

# Create your views here.
@login_required
def show_credit(request):
    form = CreditApplicationForm()
    if request.method=='POST':
        form = CreditApplicationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
    return render(request,'credit/credit.html',{'form':form})

def index(request):
    return render(request,'loan/index.html')


def thanks(request):

    return render(request,'credit/response.html',{'name':'name'})