from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import MyModel 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



# def homepage(request):
#     output=0
#     if request.method=='POST':
#         n1=float(request.POST.get('input1',0))
#         n2=float(request.POST.get('input2'))
#         output=n1+n2
#     return render(request,"home.html",{'output':output})
@login_required(login_url='login')
def homepage(request):
    if request.method == "POST":
        n1 = request.POST.get('username')
        n2 = request.POST.get('email')
        n3 = request.POST.get('password')
        
        my_user=User.objects.create_user(n1,n2,n3)
        my_user.save()
    
    return render(request,"home.html")




def Register(request):
    if request.method == "POST":
        n1 = request.POST.get('first')
        n2 = request.POST.get('last')
        n3 = request.POST.get('username')
        n4 = request.POST.get('city')
        n5 = request.POST.get('state')
        n6 = request.POST.get('zip')

        my_user = MyModel(first=n1, last=n2, username=n3, city=n4, state=n5, zip=n6)
        my_user.save()
        print("submitted")  # Print "submitted" when the form is submitted

    return render(request, "register.html")



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render(request,"landing.html")
        else:
            error_message = 'Wrong username or password'
            return JsonResponse({'success': False, 'error_message': error_message})


    return render(request,'home.html')
def landingpage(request):
    
    return render(request,"landing.html")
def logoutview(request):
    logout(request)
    return render(request,'home.html')
    