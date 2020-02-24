from django.shortcuts import render,redirect

from .models import News
from .forms import NewsForm

def home_view(request):
    news = News.objects.all()
    return render(request,'index.html',{'news':news})

def create_new(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect(home_view)
    else:
        form = NewsForm()
        context = {
            'form':form
        }
        return render(request,'form.html',context)