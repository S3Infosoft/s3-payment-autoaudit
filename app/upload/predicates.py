import rules
from math import floor

MMT_Commission_Percentage = 0.2

@rules.predicate
def MMT1_Commission_Check(obj):
    return obj['MMT_Commission'] == floor(MMT_Commission_Percentage * obj['Hotel_Gross_Price'])

@rules.predicate
def MMT2_Commission_Check(obj):
    return float(obj['Commission_Charges']) == MMT_Commission_Percentage * obj['Room_Charges']

@rules.predicate
def Booking_Commission_Check(obj):
    return float(obj['Commission_amount']) == round((obj['Commission'] / 100) * obj['Final_amount'],2) 

@rules.predicate
def Razorpay_Commission_Check(obj):
    return False

@rules.predicate
def Mswipe_Commission_Check(obj):
    return False

@rules.predicate
def Atom_Commission_Check(obj):
    return False

@rules.predicate
def Bank_Commission_Check(obj):
    if obj['Deposit_Amt'] == 0.00:
        return True
    return False
