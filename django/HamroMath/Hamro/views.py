from django.shortcuts import render
from django.http import HttpResponse

def small(request):
    
    return render(request,"index.html")
