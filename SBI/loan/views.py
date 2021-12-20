from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import LoanApplicationForm
from .models import LoanApplication
import random

def thanks(request):
    refernce_no = random_digits(1)
    return render(request,'loan/response.html',{'refernce_no':refernce_no})

def random_digits(n):
    num = range(111111111 ,999999999999)
    lst = random.sample(num, n)
    return str(lst).strip('[]')

@login_required
def show_loan(request):
    form = LoanApplicationForm()
    if request.method=='POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
    return render(request,'loan/loanform.html',{'form':form})

@login_required
def show_data(request):
    data = LoanApplication.objects.all()     # ORM Query to fetch data
    return render(request, 'loan/showdata.html',{'data':data})

def logout(request):
    return render(request,'authapp/logout.html')


def signup(request):
    form = SignupForm()
    if request.method=='POST':
        form =SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})

