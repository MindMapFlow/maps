from django.shortcuts import render
from django.views.generic import DeleteView, DetailView
from .models import SubGoal
# Create your views here.
def goals(request):
    return render(request,'goals.html')

def test(request):
     return render(request,'test.html')
 
def SubGoal_detail(request):
    return render(request,'subgoal2.html')


