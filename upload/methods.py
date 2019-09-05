from django.shortcuts import render,HttpResponse
import pandas as pd
import os
import re
import datetime
from .pdfparser import parser

def Date(result,dlist):
    for i in dlist:
        if result[i] == None:
            continue
        result[i] = re.sub('-','/',result[i])
        date_patterns = ["%d/%m/%y", "%Y/%m/%d","%d/%m/%Y"]
        for pattern in date_patterns:
            try:
                result[i] = datetime.datetime.strptime(result[i], pattern).strftime('%m/%d/%Y')
            except:
                pass
    return result

def DateTime(result,dlist):
    for i in dlist:
        if result[i] == None:
            continue
        result[i] = re.sub('-','/',result[i])
        date_patterns = ['%d/%m/%y %H:%M', "%Y/%m/%d %H:%M"]
        for pattern in date_patterns:
            try:
                result[i] = datetime.datetime.strptime(result[i],pattern).strftime('%m/%d/%Y %H:%M')
            except:
                pass
    return result

def Dictionary(result):
    d = dict()
    for i in result:
        s = re.sub(r'[()\s?/\.%\-@&()]','_',i)
        s = re.sub(r'_+','_',s)
        s = s.strip('_')
        d[s] = result[i]
    return d

def process(FileName,Type):
    if Type == 1:
        return Type1(FileName)
    elif Type == 2:
        return Type2(FileName)
    elif Type == 3:
        return Type3(FileName)
    elif Type == 4:
        return Type4(FileName)
    elif Type == 5:
        return Type5(FileName)
    elif Type == 6:
        return Type6(FileName)
    else:
        return Type7(FileName)     

def Type1(FileName):
    result = parser(FileName) 
    if result == -1:
        return result   
    result = Dictionary(result)
    fields = ('Booking_ID','No_of_nights','Check_In','Check_Out','Room','Night','Hotel_Sell_Price','Extra_Adult_Child_Charge','Hotel_Gross_Price','MMT_Commission','GST_18_Including_IGST_or_SGST_CGST','MMT_to_Pay_Hotel_A_B','GST_on_hotel_accommodation_charges_by_Ecommerce_Operator','Primary_Guest','E_mail','Contact_No','Room_Category','Meal_Plan')
    for i in result:
        if i not in fields:
            return -1
    result1 = list()
    for k,v in result.items():
        if v == 0.0:
            result[k] = None
    result1.append(result)
    return result1


def Type2(FileName):
    dlist = ['Check_in','Check_out','Booked_On','Payment_Date']
    try:
        result = pd.read_csv(FileName)
    except:
        return -1
    result1 = list()
    fields = ('BookingID','Check_in','Check_out','Booked_On','PAH_Booking','Amount_to_be_collected_from_customer_only_for_PAH_booking','Payable_Amount','Nett_Payable_to_Hotel','Customer_Name','Booking_Status','Payment_Status','Booking_Vendor','Vendor_Booking_ID','Parent_Booking_ID_only_for_Cart_booking','No_of_Rooms','No_of_Nights','Room_Charges','Extra_Adult_Child_Charges','Hotel_Taxes','Hotel_Gross_Charges','Commission_Charges','GST_Charges','Commission_Including_GST','Amount_Paid','Payment_Date','Payment_Id','Bank_Ref_VCC_No','Amount_adjusted','Adjustment_ID')
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for i in result:
            if i not in fields:
                return -1
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = Date(res,dlist)
        result1.append(res)
    return result1
    

def Type3(FileName):
    fields = ('Reservation_number','Booked_on','Arrival','Departure','Booker_name','Guest_name','Rooms','Persons','Room_nights','Commission','Original_amount','Final_amount','Commission_amount','Status','Guest_request','Currency','Hotel_id')
    dlist = ['Arrival','Departure']
    try:
        result = pd.read_csv(FileName)
    except:
        return -1
    result1 = list()
    for i in range(result.shape[0]):    
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for i in result:
            if i not in fields:
                return -1
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = Date(res,dlist)
        result1.append(res)
    return result1 

def Type4(FileName):
    fields = ('entity_id','TYPE','debit','credit','amount','currency','fee','tax','on_hold','settled','created_at','settled_at','settlement_id','description','notes','payment_id','settlement_utr','order_id','order_receipt','method','issuer_name','card_network','card_issuer','card_type','dispute_id')
    dlist = ['created_at','settled_at']
    try:
        result = pd.read_csv(FileName)
    except:
        return -1
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for i in result:
            if i not in fields:
                return -1
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = DateTime(res,dlist)
        result1.append(res)
    return result1 

def Type5(FileName):
    fields = ('CustomerCode','MerchantName','TID','IFSC','RR_NO','Stan_No','Interchange','CardNo','CardType','TxnDate','PaymentDate','PaymentRemarks1','K30_PRORATA_AMT','K30_Benefit_Received','TxnAmt','MdrMswipePer','MdrValue','GST','TDS_Amount','Deduction','Conveyance_fees_Rate','Conveyance_fees_Amount','Conveyance_fees_GST','NetAmt','Rent','Adjustment','FinalPayment','LoanDeductionRate','LoanDeductionAmount','AdditionalRecovery','FinalPaymentToMeAfterLoanDeduction','FinalPaymentToLoanProvider','REMARKS','Mswipe_Ref_No','NEFT_Ref_No','ARN','Lender_UTR_No','Lender_Payment_Date','Approval_No','Invoice_no','RowId','Cust_GroupCustCode','StoreCode','Cust_Device_Id','PaymentRemarks2')
    try:
        result = pd.read_excel(FileName)
    except:
        return -1
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for i in result:
            if i not in fields:
                return -1
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        result1.append(res)
    return result1  


def Type6(FileName):
    fields = ('Sr_no','Merchant_Name','DBA_Name','Merchant_Id','TID','Atom_Txn_ID','RRN','Auth_Code','Currency','Txn_Date','Txn_Type','Txn_Status','Recon_Status','Setteled_Date','Batch_number','Payment_Date','Amount','MSF','GST','GST_Slab','Cash_POS_Incent','net_Amount','Local_Intl','mcc','City','Card_Number')
    dlist = ['Setteled_Date','Payment_Date']
    try:
        result = pd.read_csv(FileName)
    except:
        return -1
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for i in result:
            if i not in fields:
                return -1
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = Date(res,dlist)
        res = DateTime(res,['Txn_Date'])
        for i in res:
            s = re.match('GST.*',i)
            if s:
                break
        s = s.group(0)
        res['GST'] = res[s]
        res.pop(s)
        s = s.split('_')
        res['GST_Slab'] = s[1]
        result1.append(res)
    print(res)
    return result1  

def Type7(FileName):
    try:
        df = pd.read_excel(FileName)
    except:
        return -1
    s = 'Statement Summary'
    d = df.loc[24].to_dict()
    l = dict()
    for i in d:
        l[d[i]] = '0'
    r = Dictionary(l)
    l = ['Transaction_Date','Transaction_Details','Cheque_ID','Value_Date','Withdrawl_Amt','Deposit_Amt','Balance_INR']
    for i in r:
        if i not in l:
            return -1
    i = 25
    while s != df.loc[i][0]:
        i = i + 1
    result1 = list()
    for j in range(25,i):
        res = df.loc[j].fillna(0)
        res = res.to_dict()
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        c = 0
        result = dict()
        for v in res.values():
            result[l[c]] = v
            c = c + 1
        result = Date(result,['Transaction_Date','Value_Date'])
        if result['Withdrawl_Amt'] == None:
            result['Withdrawl_Amt'] = 0
        if result['Deposit_Amt'] == None:
            result['Deposit_Amt'] = 0
        result1.append(result)
    return result1
