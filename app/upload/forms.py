from django import forms
from .models import Type1, Type2, Type3, Type4, Type5, Type6, Type7, Type8, Type9, Customer, CustomerCheckIn, CashEntry

FILE_TYPES = ((1, 'Make My Trip Voucher PDF'),
              (2, 'Make My Trip Transaction CSV'),
              (3, 'Booking.com CSV'),
              (4, 'RazorPay CSV'),
              (5, 'mSwipe XLS'),
              (6, 'Atom CSV'),
              (7, 'Bank XLS'),
              (8, 'Bank ICICI'),
              (9, 'mSwipe2 CSV'))



class LoginForm(forms.Form):
    Name = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)


class FileUploadForm(forms.Form):
    filename = forms.FileField()
    type = forms.ChoiceField(widget=forms.RadioSelect(),choices=FILE_TYPES)


class Type1Form(forms.ModelForm):
    class Meta:
        model = Type1
        fields = ('Booking_ID', 'No_of_nights', 'Check_In', 'Check_Out','Room','Night','Hotel_Sell_Price','Extra_Adult_Child_Charge','Hotel_Gross_Price','MMT_Commission','GST_18_Including_IGST_or_SGST_CGST','MMT_to_Pay_Hotel_A_B','GST_on_hotel_accommodation_charges_by_Ecommerce_Operator','Primary_Guest','E_mail','Contact_No','Room_Category','Meal_Plan')


class Type2Form(forms.ModelForm):
    class Meta:
        model = Type2
        fields = ('BookingID','Check_in','Check_out','Booked_On','PAH_Booking','Amount_to_be_collected_from_customer_only_for_PAH_booking','Payable_Amount','Nett_Payable_to_Hotel','Customer_Name','Booking_Status','Payment_Status','Booking_Vendor','Vendor_Booking_ID','Parent_Booking_ID_only_for_Cart_booking','No_of_Rooms','No_of_Nights','Room_Charges','Extra_Adult_Child_Charges','Hotel_Taxes','Hotel_Gross_Charges','Commission_Charges','GST_Charges','Commission_Including_GST','Amount_Paid','Payment_Date','Payment_Id','Bank_Ref_VCC_No','Amount_adjusted','Adjustment_ID')


class Type3Form(forms.ModelForm):
    class Meta:
        model = Type3
        fields = ('Reservation_number','Booked_on','Arrival','Departure','Booker_name','Guest_name','Rooms','Persons','Room_nights','Commission','Original_amount','Final_amount','Commission_amount','Status','Guest_request','Currency','Hotel_id')


class Type4Form(forms.ModelForm):
    class Meta:
        model = Type4
        fields = ('entity_id','TYPE','debit','credit','amount','currency','fee','tax','on_hold','settled','created_at','settled_at','settlement_id','description','notes','payment_id','settlement_utr','order_id','order_receipt','method','issuer_name','card_network','card_issuer','card_type','dispute_id')


class Type5Form(forms.ModelForm):
    class Meta:
        model = Type5
        fields = ('CustomerCode','MerchantName','TID','IFSC','RR_NO','Stan_No','Interchange','CardNo','CardType','TxnDate','PaymentDate','PaymentRemarks1','K30_PRORATA_AMT','K30_Benefit_Received','TxnAmt','MdrMswipePer','MdrValue','GST','TDS_Amount','Deduction','Conveyance_fees_Rate','Conveyance_fees_Amount','Conveyance_fees_GST','NetAmt','Rent','Adjustment','FinalPayment','LoanDeductionRate','LoanDeductionAmount','AdditionalRecovery','FinalPaymentToMeAfterLoanDeduction','FinalPaymentToLoanProvider','REMARKS','Mswipe_Ref_No','NEFT_Ref_No','ARN','Lender_UTR_No','Lender_Payment_Date','Approval_No','Invoice_no','RowId','Cust_GroupCustCode','StoreCode','Cust_Device_Id','PaymentRemarks2')


class Type6Form(forms.ModelForm):
    class Meta:
        model = Type6
        fields = ('Sr_no','Merchant_Name','DBA_Name','Merchant_Id','TID','Atom_Txn_ID','RRN','Auth_Code','Currency','Txn_Date','Txn_Type','Txn_Status','Recon_Status','Setteled_Date','Batch_number','Payment_Date','Amount','MSF','GST','GST_Slab','Cash_POS_Incent','net_Amount','Local_Intl','mcc','City','Card_Number')


class Type7Form(forms.ModelForm):
    class Meta:
        model = Type7
        fields = ('Transaction_Date','Transaction_Details','Cheque_ID','Value_Date','Withdrawl_Amt','Deposit_Amt','Balance_INR')


class Type8Form(forms.ModelForm):
    class Meta:
        model = Type8
        fields = "__all__"


class Type9Form(forms.ModelForm):
    class Meta:
        model = Type9
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = "type1", "type9", "type8"

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Customer Name"
        }
        self.fields["email"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Email"
        }
        self.fields["phone"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Phone No."
        }
        self.fields["id_from_mvr"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter ID From MVR"
        }
        self.fields["notes"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Notes"
        }


class CustomerCheckInForm(forms.ModelForm):
    class Meta:
        model = CustomerCheckIn
        fields = "__all__"
        widgets = {
            'checkin_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'checkout_date': forms.DateInput(format=('%m/%d/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerCheckInForm, self).__init__(*args, **kwargs)
        self.fields["customer"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Customer Name"
        }
        self.fields["expected_amount"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Expected Amount",
            "step": ".01"
        }
        self.fields["realised_amount"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Realised Amount"
        }
        self.fields["notes"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Notes"
        }


class CashEntryForm(forms.ModelForm):
    class Meta:
        model = CashEntry
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(format=('%d/%m/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
            }

    def __init__(self, *args, **kwargs):
        super(CashEntryForm, self).__init__(*args, **kwargs)
        self.fields["customer"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Customer Name"
        }
        self.fields["cash_amount"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Cash Amount",
            "step": ".01"
        }
        self.fields["details"].widget.attrs = {
            "class": "form-control",
            "placeholder": "Enter Details"
        }

