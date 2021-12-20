from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SavingApplicationForm
# Create your views here.
def thanks(request):
    return render(request,'saving/response.html')

@login_required
def show_saving(request):
    form = SavingApplicationForm()
    if request.method == 'POST':
        form = SavingApplicationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thanks(request)
    return render(request, 'saving/saving.html',{'form':form})

def index(request):
    return render(request, 'saving/index.html')