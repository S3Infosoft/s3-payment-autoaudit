from django.shortcuts import render,HttpResponse
from .forms import LoginForm,FileUploadForm,Type1Form,Type2Form,Type3Form,Type4Form,Type5Form,Type6Form,Type7Form
from .methods import process
from .models import Type1,Type2,Type3,Type4,Type5,Type6,Type7
from .rules import manual_check
import sys
import os



def TypeForm(res,Type):
    if Type == 1:
        return Type1Form(res)
    elif Type == 2:
        return Type2Form(res)
    elif Type == 3:
        return Type3Form(res)
    elif Type == 4:
        return Type4Form(res)
    elif Type == 5:
        return Type5Form(res)
    elif Type == 6:
        return Type6Form(res)
    else:
        return Type7Form(res)    


def data_from_db():
    heading = ['Make My Trip Voucher PDF','Make My Trip Transaction CSV','Booking.com CSV','RazorPay CSV','mSwipe XLS','Atom CSV','Bank XLS']
    data = dict()
    res = list(Type1.objects.values())
    data[heading[0]] = res
    res = list(Type2.objects.values())
    data[heading[1]] = res
    res = list(Type3.objects.values())
    data[heading[2]] = res
    res = list(Type4.objects.values())
    data[heading[3]] = res
    res = list(Type5.objects.values())
    data[heading[4]] = res
    res = list(Type6.objects.values())
    data[heading[5]] = res
    res = list(Type7.objects.values())
    data[heading[6]] = res
    return data 

def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        name = request.POST['Name']
        password = request.POST['Password']
        print(name,password)
        if name == 'Admin' and password == 'root@123':
            return render(request,'home.html',{'data':data_from_db(),'flag':'True'})      
        else:
            form = LoginForm()
            return render(request,'login.html',{'form':form})
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def home(request):
    return render(request,'home.html',{'data':data_from_db(),'flag':'True'})

def fileupload(request):
    if request.method =='POST':
        form = FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            FileName = request.FILES['FileName']
            Type = int(request.POST['Type'])
            try:
                res = process(FileName,Type)
            except:
                return render(request,'home.html',{'form':FileUploadForm(),'flag':'null','error':'True'})
            if res == -1:
                return render(request,'home.html',{'form':FileUploadForm(),'flag':'null','error':'True'})
            for d in res: 
                try:
                    form1 = TypeForm(d,Type)  
                    if form1.is_valid():
                        form1.save()
                except Exception as e:
                    print(e)
            return render(request,'home.html',{'data':data_from_db(),'flag':'True'})        
    else:
        form = FileUploadForm()
        return render(request,'home.html',{'form':form,'flag':'null'})

def manualaudit(request):
    return render(request,'home.html',{'data':manual_check(),'flag':'False'})
    


