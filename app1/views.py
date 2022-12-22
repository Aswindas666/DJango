from django.shortcuts import render,HttpResponse
from .models import Student,Teacher
# Create your views here.

def Home(request):
    tea=Teacher.objects.all()
    stud=Student.objects.all()
    obj=Student.objects.get(id=3)
    obj1=Student.objects.filter(name='kichu')
    return render(request,'home.html',{'ob':stud,
                                        'data':tea,
                                        'id':obj,
                                        'obj1':obj1
                                         })
    

def Next(request):
    # user= request.GET.get('username')
    # pwd= request.GET.get('password')
    
    if request.method=='POST':
        user= request.POST.get('username')
        pwd= request.POST.get('password')
        print(user,pwd)
    return render(request,'next.html')

def index(request):
    return render(request,'index.html')