from django.db import models
from django.urls import reverse
from django.forms import ModelForm


class Type1(models.Model):
    Booking_ID = models.CharField(max_length=30, unique=True)
    No_of_nights = models.IntegerField(null=True, blank=True)
    Check_In = models.DateTimeField(max_length=30, null=True,blank=True)
    Check_Out = models.DateTimeField(max_length=30,null=True,blank=True)
    Room = models.IntegerField(null=True, blank=True)
    Night = models.IntegerField(null=True,blank=True)
    Hotel_Sell_Price = models.CharField(max_length = 30,null=True,blank=True)
    Extra_Adult_Child_Charge = models.IntegerField(null=True,blank=True)
    Hotel_Gross_Price = models.IntegerField(null=True,blank=True)
    MMT_Commission = models.IntegerField(null=True,blank=True)
    GST_18_Including_IGST_or_SGST_CGST = models.IntegerField(null=True,blank=True)
    MMT_to_Pay_Hotel_A_B = models.IntegerField(null=True,blank=True)
    GST_on_hotel_accommodation_charges_by_Ecommerce_Operator = models.IntegerField(null=True,blank=True)
    Primary_Guest = models.CharField(max_length = 30,null=True,blank=True)
    E_mail = models.CharField(max_length = 30,null=True,blank=True)
    Contact_No = models.CharField(max_length = 50,null=True,blank=True)
    Room_Category = models.CharField(max_length = 30,null=True,blank=True)
    Meal_Plan = models.CharField(max_length = 30,null=True,blank=True)

class Type2(models.Model):
    BookingID = models.IntegerField(unique = True)
    Check_in = models.DateField(null=True,blank=True)
    Check_out = models.DateField(null=True,blank=True)
    Booked_On = models.DateField(null=True,blank=True)
    PAH_Booking = models.CharField(max_length = 3,null=True,blank=True)
    Amount_to_be_collected_from_customer_only_for_PAH_booking = models.IntegerField(null=True,blank=True)
    Payable_Amount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Nett_Payable_to_Hotel = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Customer_Name = models.CharField(max_length = 30,null=True,blank=True)
    Booking_Status = models.CharField(max_length = 30,null=True,blank=True)
    Payment_Status = models.CharField(max_length = 30,null=True,blank=True)
    Booking_Vendor = models.CharField(max_length = 30,null=True,blank=True)
    Vendor_Booking_ID = models.CharField(max_length = 30,null=True,blank=True)
    Parent_Booking_ID_only_for_Cart_booking = models.CharField(max_length = 30, null=True,blank=True)    
    No_of_Rooms = models.IntegerField(null=True,blank=True)
    No_of_Nights = models.IntegerField(null=True,blank=True)
    Room_Charges = models.IntegerField(null=True,blank=True)
    Extra_Adult_Child_Charges = models.IntegerField(null=True,blank=True)
    Hotel_Taxes = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Hotel_Gross_Charges = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Commission_Charges = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    GST_Charges = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Commission_Including_GST = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Amount_Paid = models.IntegerField(null=True,blank=True)
    Payment_Date = models.DateField(null=True,blank=True)
    Payment_Id = models.CharField(max_length = 50,null=True,blank=True)
    Bank_Ref_VCC_No = models.CharField(max_length = 30,null=True,blank=True)
    Amount_adjusted = models.IntegerField(null=True,blank=True)
    Adjustment_ID = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)


class Type3(models.Model):
    Reservation_number = models.IntegerField(unique = True)
    Booked_on = models.CharField(max_length = 50,null=True,blank=True)
    Arrival = models.DateField(null=True,blank=True)
    Departure = models.DateField(null=True,blank=True)
    Booker_name = models.CharField(max_length = 30,null=True,blank=True)
    Guest_name = models.CharField(max_length = 30,null=True,blank=True)
    Rooms = models.IntegerField(null=True,blank=True)
    Persons = models.IntegerField(null=True,blank=True)
    Room_nights = models.IntegerField(null=True,blank=True)
    Commission = models.IntegerField(null=True,blank=True)
    Original_amount = models.IntegerField(null=True,blank=True)
    Final_amount = models.IntegerField(null=True,blank=True)
    Commission_amount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Status = models.CharField(max_length = 30,null=True,blank=True)
    Guest_request = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Currency = models.CharField(max_length = 30,null=True,blank=True)
    Hotel_id = models.IntegerField(null=True,blank=True)


class Type4(models.Model):
    entity_id = models.CharField(max_length = 30, unique = True,blank=True)
    TYPE = models.CharField(max_length = 30,null=True,blank=True)
    debit = models.IntegerField(null=True,blank=True)
    credit = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    currency = models.CharField(max_length = 30,null=True,blank=True)
    fee = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    tax = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    on_hold = models.IntegerField(null=True,blank=True)
    settled = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(null=True,blank=True)
    settled_at = models.DateTimeField(null=True,blank=True)
    settlement_id = models.CharField(max_length = 30,null=True,blank=True)
    description = models.CharField(max_length = 30,null=True,blank=True)
    notes = models.CharField(max_length = 30,null=True,blank=True)
    payment_id = models.CharField(max_length = 30,null=True,blank=True)
    settlement_utr = models.CharField(max_length = 30,null=True,blank=True)
    order_id = models.CharField(max_length = 30,null=True,blank=True)
    order_receipt = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    method = models.CharField(max_length = 30,null=True,blank=True)
    issuer_name = models.CharField(max_length = 30,null=True,blank=True)
    card_network = models.CharField(max_length = 30,null=True,blank=True)
    card_issuer = models.CharField(max_length = 30,null=True,blank=True)
    card_type = models.CharField(max_length = 30,null=True,blank=True)
    dispute_id = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)


class Type5(models.Model):
    CustomerCode = models.IntegerField(null=True)
    MerchantName = models.CharField(max_length = 30,null=True,blank=True)
    TID = models.IntegerField(null=True,blank=True)
    IFSC = models.CharField(max_length = 30,null=True,blank=True)
    RR_NO = models.IntegerField(null=True,blank=True)
    Stan_No = models.IntegerField(null=True,blank=True)
    Interchange = models.CharField(max_length = 30,null=True,blank=True)
    CardNo = models.CharField(max_length = 30,null=True,blank=True)
    CardType = models.CharField(max_length = 30,null=True,blank=True)
    TxnDate = models.CharField(max_length = 30,null=True)
    PaymentDate = models.CharField(max_length = 30,null=True,blank=True)
    PaymentRemarks1 = models.CharField(max_length = 30,null=True,blank=True)
    K30_PRORATA_AMT = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    K30_Benefit_Received = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    TxnAmt = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    MdrMswipePer = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    MdrValue = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    GST = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    TDS_Amount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Deduction = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Conveyance_fees_Rate = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Conveyance_fees_Amount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Conveyance_fees_GST = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    NetAmt = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Rent = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Adjustment = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    FinalPayment = models.DecimalField(max_digits = 20,decimal_places = 2,null=True)
    LoanDeductionRate = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    LoanDeductionAmount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    AdditionalRecovery = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    FinalPaymentToMeAfterLoanDeduction = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    FinalPaymentToLoanProvider = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    REMARKS = models.CharField(max_length = 30,null=True,blank=True)
    Mswipe_Ref_No = models.IntegerField(null=True,blank=True)
    NEFT_Ref_No = models.IntegerField(null=True,blank=True)
    ARN = models.IntegerField(null=True,blank=True)
    Lender_UTR_No = models.IntegerField(null=True,blank=True)
    Lender_Payment_Date = models.CharField(max_length = 30,null=True,blank=True)
    Approval_No = models.IntegerField(null=True,blank=True)
    Invoice_no = models.CharField(max_length = 30,null=True,blank=True)
    RowId = models.CharField(max_length = 30,null=True,blank=True)
    Cust_GroupCustCode = models.CharField(max_length = 30,null=True,blank=True)
    StoreCode = models.CharField(max_length = 30,null=True,blank=True)
    Cust_Device_Id = models.IntegerField(null=True,blank=True)
    PaymentRemarks2 = models.CharField(max_length = 30,null=True,blank=True)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['CustomerCode','TxnDate','FinalPayment'], name='type5_unique'),]

    
class Type6(models.Model):
    Sr_no = models.IntegerField(null=True,blank=True)
    Merchant_Name = models.CharField(max_length = 30,null=True,blank=True)
    DBA_Name = models.CharField(max_length = 30,null=True,blank=True)
    Merchant_Id = models.IntegerField(null=True,blank=True)
    TID = models.IntegerField(null=True,blank=True)
    Atom_Txn_ID = models.DecimalField(max_digits = 20,decimal_places = 2,null=True)
    RRN = models.DecimalField(max_digits = 20,decimal_places = 2,null=True)
    Auth_Code = models.IntegerField(null=True)
    Currency = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Txn_Date = models.DateTimeField(null=True)
    Txn_Type = models.IntegerField(null=True,blank=True)
    Txn_Status = models.IntegerField(null=True,blank=True)
    Recon_Status = models.CharField(max_length = 30,null=True,blank=True)
    Setteled_Date = models.DateField(null=True,blank=True)
    Batch_number = models.IntegerField(null=True,blank=True)
    Payment_Date = models.DateField(null=True,blank=True)
    Amount = models.IntegerField(null=True,blank=True)
    MSF = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    GST = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    GST_Slab = models.IntegerField(null=True,blank=True)
    Cash_POS_Incent = models.IntegerField(null=True,blank=True)
    net_Amount = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    Local_Intl = models.CharField(max_length = 30,null=True,blank=True)
    mcc = models.IntegerField(null=True,blank=True)
    City = models.CharField(max_length = 30,null=True,blank=True)
    Card_Number = models.CharField(max_length = 30,null=True,blank=True)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['Atom_Txn_ID','RRN','Auth_Code','Txn_Date'], name='type6_unique'),]


class Type7(models.Model):
    Transaction_Date = models.DateField(null=True)
    Transaction_Details = models.CharField(max_length = 50,null=True)
    Cheque_ID = models.CharField(max_length = 30,null=True,blank=True)
    Value_Date = models.DateField(null=True,blank=True)
    Withdrawl_Amt = models.DecimalField(max_digits = 20,decimal_places = 2,null=True)
    Deposit_Amt = models.DecimalField(max_digits = 20,decimal_places = 2,null=True)
    Balance_INR = models.DecimalField(max_digits = 20,decimal_places = 2,null=True,blank=True)
    
    class Meta:
        constraints = [ models.UniqueConstraint(fields=['Transaction_Date','Transaction_Details','Withdrawl_Amt','Deposit_Amt'], name='type7_unique'),]


class Type8(models.Model):
    """These are the details of the ICICI bank"""
    transaction_id = models.CharField(max_length=25, primary_key=True)
    transaction_value_date = models.DateField(null=True)
    transaction_posted_date = models.DateField(null=True)
    mode_of_payment = models.CharField(max_length=100)
    credit = models.CharField(max_length=7)
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.transaction_id


class Type9(models.Model):
    """These are the details of mswipe2 i.e. CCard (mode of payment) by ICICI bANK"""
    id = models.CharField(max_length=25, primary_key=True)
    date = models.DateTimeField(null=True)
    mobile = models.CharField(max_length=15)
    consumer = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    mode = models.CharField(max_length=30)
    amount = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    cash_at_pos = models.CharField(max_length=250)
    txn_type = models.CharField(max_length=150)
    auth_code = models.CharField(max_length=100)
    card = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    brand_type = models.CharField(max_length=200)
    card_txn_type = models.CharField(max_length=200)
    rrn = models.CharField(max_length=80)
    invoice = models.CharField(max_length=20)
    device_serial = models.CharField(max_length=100)
    status = models.CharField(max_length=200)
    settled_on = models.DateTimeField(null=True)
    mid = models.CharField(max_length=250)
    tid = models.CharField(max_length=300)
    batch = models.CharField(max_length=150)
    ref = models.CharField(max_length=100)
    payer = models.CharField(max_length=100)
    tid_location = models.CharField(max_length=150)
    dx_mode = models.CharField(max_length=200)
    acquiring_bank = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    id_from_mvr = models.CharField(max_length=40)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})


class CustomerCheckIn(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    checkin_date = models.DateField(null=True)
    checkout_date = models.DateField(null=True)
    expected_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    realised_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse('checkin_detail', kwargs={'pk': self.pk})


class CashEntry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cash_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    date = models.DateField(null=True)
    details = models.CharField(max_length=30)

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse('cashentry_detail', kwargs={'pk': self.pk})
