
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
def aboutus(request):
    return HttpResponse("This is home page")
def coursedetail(request,courseid):
    return HttpResponse(courseid)

# def homepage(request):
#     data={
#         'title':'my home page',
#         'bdata':'welcome to my page',
#         'clist':['php','java','django'],
#         'student_details':[
#             {'name':'harish','phone':7453966532},
#              {'name':'kabir','phone':7478966532}
                
            
#         ]
#     }
#     return render(request,"index.html",data)
def landing_page(request):
    return render(request,"Landing_page.html")

def ports(request):
    return render(request,"portfolio.html")

def cals(request):
    return render(request,"calculator.html")

def homes(request):
    return render(request,"home.html")

# def userForm(request):
#     finalans=0
#     try:
#         n1=request.GET['names']
#         n2=request.GET['gmails']
        
#         finalans=n1+n2
#         
#     except:
#         pass
#     return render(request,"userform.html",{'output':finalans})


def userFormp(request):
    finalans=0
    try:
        n1=request.POST['names']
        n2=request.POST['gmails']
        
        finalans=n1+n2
        # return HttpResponseRedirect('/calculator/')
    except:
        pass
    return render(request,"userform.html",{'output':finalans})
def submit(request):
    return HttpResponse(request)

def calcul(request):
    c=''
    try: 
        if request.method=="POST":
            n1=eval(request.POST.get('value1'))
            n2=eval(request.POST.get('value2'))
            oper=request.POST.get('operation')
            if oper=="+":
                c=n1+n2
            elif oper=="-":
                c=n1-n2
            elif oper=="*":
                c=n1*n2
            elif oper=="/":
                c=n1/n2
    except:
        print("invalid operator")
    print(c)
    return render(request,"calculators.html",{'c':c})
            
        
        