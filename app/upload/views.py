from django.db.models.functions import datetime
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .forms import LoginForm, FileUploadForm, Type1Form, Type2Form, Type3Form, Type4Form, Type5Form, Type6Form, \
    Type7Form, Type8Form, Type9Form, CustomerForm, CustomerCheckInForm, CashEntryForm
from .methods import process
from .models import Type1, Type2, Type3, Type4, Type5, Type6, Type7, Customer, CustomerCheckIn, CashEntry
from .rules import manual_check
from .excelparser import xlparser
from .csvparser import csvparser
from .master_data import provide_master_data


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


def link_customer(request, pk, type_, data_id):
    if type_[-1] == "1":
        pass
    elif type_[-1] == "8":
        Customer.objects.get(pk=pk).type8.add(data_id)
    elif type_[-1] == "9":
        Customer.objects.get(pk=pk).type9.add(data_id)
    return redirect("customer_detail", pk)


def send_master_data(request, month, year):
    return JsonResponse(provide_master_data(month, year))


def icici_view(request):
    return render(request, "icici.html")


def mswipe_view(request):
    return render(request, "mswipe.html")


def TypeForm(res, Type):
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
    heading = ['Make My Trip Voucher PDF', 'Make My Trip Transaction CSV', 'Booking.com CSV', 'RazorPay CSV',
               'mSwipe XLS', 'Atom CSV', 'Bank XLS']
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        name = request.POST['Name']
        password = request.POST['Password']
        print(name, password)
        if name == 'Admin' and password == 'root@123':
            return render(request, 'home.html', {'data': data_from_db(), 'flag': 'True'})
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html', {'data': data_from_db(), 'flag': 'True'})


def convert_to_datetime(datetime_: str):
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
                    return render(request, 'home.html', {'form': FileUploadForm(), 'flag': 'null', 'error': 'True'})
                if res == -1:
                    return render(request, 'home.html', {'form': FileUploadForm(), 'flag': 'null', 'error': 'True'})
                for d in res:
                    d["Check_In"] = convert_to_datetime(d.get("Check_In", "NOT FOUND"))
                    d["Check_Out"] = convert_to_datetime(d.get("Check_Out", "NOT FOUND"))

                    form1 = TypeForm(d, type_)
                    if form1.is_valid():
                        form1.save()
                    else:
                        print(form1.errors)
                        return render(request, 'home.html', {'form': form, 'flag': 'null'})
            if type_ == 8:
                dataset = xlparser(file.read())  # calling xlparser method and storing in the dataset
                for data in dataset:
                    form8 = Type8Form(data)
                    if form8.is_valid():
                        form8.save()
                    else:
                        print(form8.errors)
                return redirect('icici')
            if type_ == 9:
                dataset = csvparser(file)
                for data in dataset:
                    form9 = Type9Form(data)
                    if form9.is_valid():
                        form9.save()
                    else:
                        print(form9.errors)
                return redirect('mswipe')
            return render(request, 'home.html')
        else:
            print(form.errors)
    else:
        form = FileUploadForm()
        return render(request, 'home.html', {'form': form, 'flag': 'null'})


def manualaudit(request):
    return render(request, 'home.html', {'data': manual_check(), 'flag': 'False'})


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'Customer/create.html'

    def get_success_url(self):
        return reverse("customer_detail", kwargs={"pk": self.object.pk})


class CustomerListView(ListView):
    model = Customer
    form_class = CustomerForm
    template_name = 'Customer/list.html'
    ordering = ['-id']


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "Customer/detail.html"

    def get_context_data(self, **kwargs):
        ctx = super(CustomerDetailView, self).get_context_data(**kwargs)
        form = CustomerForm(instance=self.object)
        ctx["update_form"] = form

        return ctx


def update_customer(request, pk):
    if request.method == "POST":
        customer = Customer.objects.get(pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(customer.get_absolute_url())


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customer_list")


class CustomerCheckInCreateView(CreateView):
    model = CustomerCheckIn
    form_class = CustomerCheckInForm
    template_name = 'CustomerCheckIn/create.html'

    def get_success_url(self):
        return reverse("checkin_detail", kwargs={"pk": self.object.pk})


class CustomerCheckInListView(ListView):
    model = CustomerCheckIn
    form_class = CustomerCheckInForm
    template_name = 'CustomerCheckIn/list.html'
    ordering = ['-customer']


class CustomerCheckInDetailView(DetailView):
    model = CustomerCheckIn
    template_name = 'CustomerCheckIn/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(CustomerCheckInDetailView, self).get_context_data(**kwargs)
        form = CustomerCheckInForm(instance=self.object)
        ctx["update_form"] = form

        return ctx


def update_customercheckin(request, pk):
    if request.method == "POST":
        checkin = CustomerCheckIn.objects.get(pk=pk)
        form = CustomerCheckInForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect(checkin.get_absolute_url())


class CustomerCheckInDeleteView(DeleteView):
    model = CustomerCheckIn
    success_url = reverse_lazy("checkin_list")


class CashEntryCreateView(CreateView):
    model = CashEntry
    form_class = CashEntryForm
    template_name = 'CashEntry/create.html'

    def get_success_url(self):
        return reverse("cashentry_detail", kwargs={"pk": self.object.pk})


class CashEntryListView(ListView):
    model = CashEntry
    form_class = CashEntryForm
    template_name = 'CashEntry/list.html'
    ordering = ['-customer']


class CashEntryDetailView(DetailView):
    model = CashEntry
    template_name = 'CashEntry/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(CashEntryDetailView, self).get_context_data(**kwargs)
        form = CashEntryForm(instance=self.object)
        ctx["update_form"] = form

        return ctx


def update_cashentry(request, pk):
    if request.method == "POST":
        cashentry = CashEntry.objects.get(pk=pk)
        form = CashEntryForm(request.POST, instance=cashentry)
        if form.is_valid():
            form.save()
            return redirect(cashentry.get_absolute_url())


class CashEntryDeleteView(DeleteView):
    model = CashEntry
    success_url = reverse_lazy("cashentry_list")

