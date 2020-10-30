from django.shortcuts import render
from exam.models import que

# Create your views here.

def fun(req):
    ex = que.objects.all()
    return render(req,"ex.html",{"ex":ex})
    