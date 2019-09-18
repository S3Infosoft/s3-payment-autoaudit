import rules
from .models import Type1,Type2,Type3,Type4,Type5,Type6,Type7
from .predicates import MMT1_Commission_Check,MMT2_Commission_Check,Mswipe_Commission_Check,Razorpay_Commission_Check,Atom_Commission_Check,Bank_Commission_Check,Booking_Commission_Check

def data_from_db():
    data = dict()
    res = list(Type1.objects.values())
    data[1] = res
    res = list(Type2.objects.values())
    data[2] = res
    res = list(Type3.objects.values())
    data[3] = res
    res = list(Type4.objects.values())
    data[4] = res
    res = list(Type5.objects.values())
    data[5] = res
    res = list(Type6.objects.values())
    data[6] = res
    res = list(Type7.objects.values())
    data[7] = res
    return data 

    
def addRules():
    rules.add_rule('1',MMT1_Commission_Check)
    rules.add_rule('2',MMT2_Commission_Check)
    rules.add_rule('3',Booking_Commission_Check)
    rules.add_rule('4',Razorpay_Commission_Check)
    rules.add_rule('5',Mswipe_Commission_Check)
    rules.add_rule('6',Atom_Commission_Check)
    rules.add_rule('7',Bank_Commission_Check)


def manual_check():
    try:
        addRules()
    except:
        pass
    flag = False
    data = data_from_db()
    d = dict()
    heading = ['Make My Trip Voucher PDF','Make My Trip Transaction CSV','Booking.com CSV','RazorPay CSV','mSwipe XLS','Atom CSV','Bank XLS']
    for j in data:
        res = data[j]
        list1 = list()
        for i in res:
            if not rules.test_rule(str(j),i):
                print('OKAY!')
                list1.append(i)
        print()
        d[heading[int(j-1)]] = list1
    return d
    


