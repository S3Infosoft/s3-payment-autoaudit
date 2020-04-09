from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from .forms import LoginForm, FileUploadForm, Type1Form, Type2Form, Type3Form, Type4Form, Type5Form, Type6Form, \
    Type7Form, Type8Form
from .methods import process
from .models import Type1, Type2, Type3, Type4, Type5, Type6, Type7
from .rules import manual_check
from .excelparser import xlparser

DATE_MONTH = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def icici_view(request):
    return render(request, "icici.html")


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


def convert_to_datetime(datetime_:  str):
    time, date = datetime_.split()
    hours, mint = time.split(":")
    day, month, year = date.split("-")
    if mint[-2:] == "PM":
        hours = (int(hours) + 12) % 24
    mint = mint[:-2]
    month = DATE_MONTH[month]

    return datetime.datetime(int(year), int(month), int(day),
                             int(hours), int(mint))


def fileupload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['filename']
            type_ = int(request.POST['type'])
            if type_ == 1:
                try:
                    res = process(file, type_)
                except:
                    return render(request, 'home.html', {'form':FileUploadForm(), 'flag':'null', 'error':'True'})
                if res == -1:
                    return render(request,'home.html',{'form':FileUploadForm(),'flag':'null','error':'True'})
                for d in res:
                    d["Check_In"] = convert_to_datetime(d.get("Check_In", "NOT FOUND"))
                    d["Check_Out"] = convert_to_datetime(d.get("Check_Out", "NOT FOUND"))

                    form1 = TypeForm(d, type_)
                    if form1.is_valid():
                        form1.save()
                    else:
                        print(form1.errors)
                        return render(request,'home.html', {'form': form, 'flag': 'null'})
            if type_ == 8:
                print(file)
                dataset = xlparser(file.read())  # calling xlparser method and storing in the dataset
                for data in dataset:
                    print(data)
                    form8 = Type8Form(data)
                    if form8.is_valid():
                        form8.save()
                    else:
                        print(form8.errors)
                return redirect('icici')

            return render(request, 'home.html')
        else:
            print(form.errors)
    else:
        form = FileUploadForm()
        return render(request,'home.html',{'form':form,'flag':'null'})


def manualaudit(request):
    return render(request,'home.html',{'data':manual_check(),'flag':'False'})
