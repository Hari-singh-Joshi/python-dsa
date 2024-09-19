from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import app1Form


@login_required(login_url='login')
def homepage(request):
     return render(request,'home.html')



def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'redirect_url': '/homepage/'})
        else:
            return JsonResponse({'success': False, 'error_message': 'Wrong username or password'})

    return render(request, 'login.html')


def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return JsonResponse({'success': False, 'error_message': 'password are different'})
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render(request,'signup.html')

def logoutview(request):
     logout(request)
     return redirect('login')
 
def landing_page(request):
    return render(request,"Landing_page.html")


def cals(request):
    return render(request,"calculator.html")

    


def cons(request):
    if request.method == 'POST':
        form = app1Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = app1Form()
    return render(request, 'content.html', {'form': form})

        
   
    
