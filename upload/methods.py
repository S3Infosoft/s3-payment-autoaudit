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
        s = re.sub(r'[()\s?/\.%\-@&]','_',i)
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
    result = Dictionary(result)
    result1 = list()
    for k,v in result.items():
        if v == 0.0:
            result[k] = None
    result1.append(result)
    return result1


def Type2(FileName):
    #MakeMyTrip Transaction CSV
    #MMT_CSV_sample1_pending_payment.csv
    #MMT_CSV_sample2_payment_done.csv
    dlist = ['Check_in','Check_out','Booked_On','Payment_Date']
    FilePath = os.path.join('./upload/Files',FileName)
    result = pd.read_csv(FilePath)
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = Date(res,dlist)
        result1.append(res)
    return result1
    

def Type3(FileName):
    #Booking.com CSV
    #booking.com_sample1.csv
    dlist = ['Arrival','Departure']
    FilePath = os.path.join('./upload/Files',FileName)
    result = pd.read_csv(FilePath)
    result1 = list()
    for i in range(result.shape[0]):    
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = Date(res,dlist)
        result1.append(res)
    return result1 

def Type4(FileName):
    #RazorPay CSV
    #RP_sample1.csv
    dlist = ['created_at','settled_at']
    FilePath = os.path.join('./upload/Files',FileName)
    result = pd.read_csv(FilePath)
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        res = DateTime(res,dlist)
        result1.append(res)
    return result1 

def Type5(FileName):
    FilePath = os.path.join('./upload/Files',FileName)
    result = pd.read_excel(FilePath)
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
        for k,v in res.items():
            if v == 0.0:
                res[k] = None
        result1.append(res)
    return result1  


def Type6(FileName):
    #Atom CSV
    #atom_sample1.csv
    dlist = ['Setteled_Date','Payment_Date']
    FilePath = os.path.join('./upload/Files',FileName)
    result = pd.read_csv(FilePath)
    result1 = list()
    for i in range(result.shape[0]):
        res = result.loc[i].fillna(0)
        res = res.to_dict()
        res = Dictionary(res)
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
    FilePath = os.path.join('./upload/Files',FileName)
    df = pd.read_excel(FilePath)
    i = 25
    s = 'Statement Summary'
    while s != df.loc[i][0]:
        i = i + 1
    l = ['Transaction_Date','Transaction_Details','Cheque_ID','Value_Date','Withdrawl_Amt','Deposit_Amt','Balance_INR']
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


def handle_uploaded_file(f,Type):
    if Type == Type2 or Type == Type3 or Type == Type4 or Type == Type6:   
        with open('./upload/Files/Upload.csv', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return 'Upload.csv'
    if Type == Type5 or Type == Type7:
        with open('./upload/Files/Upload1.xls', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return 'Upload1.xls'
    else:
        with open('./upload/Files/Upload2.pdf', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return 'Upload2.pdf'
