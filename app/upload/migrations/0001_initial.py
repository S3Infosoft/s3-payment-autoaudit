# Generated by Django 2.2.5 on 2019-09-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_ID', models.CharField(max_length=30, unique=True)),
                ('No_of_nights', models.IntegerField(blank=True, null=True)),
                ('Check_In', models.CharField(blank=True, max_length=30, null=True)),
                ('Check_Out', models.CharField(blank=True, max_length=30, null=True)),
                ('Room', models.IntegerField(blank=True, null=True)),
                ('Night', models.IntegerField(blank=True, null=True)),
                ('Hotel_Sell_Price', models.CharField(blank=True, max_length=30, null=True)),
                ('Extra_Adult_Child_Charge', models.IntegerField(blank=True, null=True)),
                ('Hotel_Gross_Price', models.IntegerField(blank=True, null=True)),
                ('MMT_Commission', models.IntegerField(blank=True, null=True)),
                ('GST_18_Including_IGST_or_SGST_CGST', models.IntegerField(blank=True, null=True)),
                ('MMT_to_Pay_Hotel_A_B', models.IntegerField(blank=True, null=True)),
                ('GST_on_hotel_accommodation_charges_by_Ecommerce_Operator', models.IntegerField(blank=True, null=True)),
                ('Primary_Guest', models.CharField(blank=True, max_length=30, null=True)),
                ('E_mail', models.CharField(blank=True, max_length=30, null=True)),
                ('Contact_No', models.CharField(blank=True, max_length=50, null=True)),
                ('Room_Category', models.CharField(blank=True, max_length=30, null=True)),
                ('Meal_Plan', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingID', models.IntegerField(unique=True)),
                ('Check_in', models.DateField(blank=True, null=True)),
                ('Check_out', models.DateField(blank=True, null=True)),
                ('Booked_On', models.DateField(blank=True, null=True)),
                ('PAH_Booking', models.CharField(blank=True, max_length=3, null=True)),
                ('Amount_to_be_collected_from_customer_only_for_PAH_booking', models.IntegerField(blank=True, null=True)),
                ('Payable_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Nett_Payable_to_Hotel', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Customer_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Booking_Status', models.CharField(blank=True, max_length=30, null=True)),
                ('Payment_Status', models.CharField(blank=True, max_length=30, null=True)),
                ('Booking_Vendor', models.CharField(blank=True, max_length=30, null=True)),
                ('Vendor_Booking_ID', models.CharField(blank=True, max_length=30, null=True)),
                ('Parent_Booking_ID_only_for_Cart_booking', models.CharField(blank=True, max_length=30, null=True)),
                ('No_of_Rooms', models.IntegerField(blank=True, null=True)),
                ('No_of_Nights', models.IntegerField(blank=True, null=True)),
                ('Room_Charges', models.IntegerField(blank=True, null=True)),
                ('Extra_Adult_Child_Charges', models.IntegerField(blank=True, null=True)),
                ('Hotel_Taxes', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Hotel_Gross_Charges', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Commission_Charges', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GST_Charges', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Commission_Including_GST', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Amount_Paid', models.IntegerField(blank=True, null=True)),
                ('Payment_Date', models.DateField(blank=True, null=True)),
                ('Payment_Id', models.CharField(blank=True, max_length=50, null=True)),
                ('Bank_Ref_VCC_No', models.CharField(blank=True, max_length=30, null=True)),
                ('Amount_adjusted', models.IntegerField(blank=True, null=True)),
                ('Adjustment_ID', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reservation_number', models.IntegerField(unique=True)),
                ('Booked_on', models.CharField(blank=True, max_length=50, null=True)),
                ('Arrival', models.DateField(blank=True, null=True)),
                ('Departure', models.DateField(blank=True, null=True)),
                ('Booker_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Guest_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Rooms', models.IntegerField(blank=True, null=True)),
                ('Persons', models.IntegerField(blank=True, null=True)),
                ('Room_nights', models.IntegerField(blank=True, null=True)),
                ('Commission', models.IntegerField(blank=True, null=True)),
                ('Original_amount', models.IntegerField(blank=True, null=True)),
                ('Final_amount', models.IntegerField(blank=True, null=True)),
                ('Commission_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Status', models.CharField(blank=True, max_length=30, null=True)),
                ('Guest_request', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Currency', models.CharField(blank=True, max_length=30, null=True)),
                ('Hotel_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.CharField(blank=True, max_length=30, unique=True)),
                ('TYPE', models.CharField(blank=True, max_length=30, null=True)),
                ('debit', models.IntegerField(blank=True, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=30, null=True)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('on_hold', models.IntegerField(blank=True, null=True)),
                ('settled', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('settled_at', models.DateTimeField(blank=True, null=True)),
                ('settlement_id', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.CharField(blank=True, max_length=30, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=30, null=True)),
                ('settlement_utr', models.CharField(blank=True, max_length=30, null=True)),
                ('order_id', models.CharField(blank=True, max_length=30, null=True)),
                ('order_receipt', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('method', models.CharField(blank=True, max_length=30, null=True)),
                ('issuer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('card_network', models.CharField(blank=True, max_length=30, null=True)),
                ('card_issuer', models.CharField(blank=True, max_length=30, null=True)),
                ('card_type', models.CharField(blank=True, max_length=30, null=True)),
                ('dispute_id', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerCode', models.IntegerField(null=True)),
                ('MerchantName', models.CharField(blank=True, max_length=30, null=True)),
                ('TID', models.IntegerField(blank=True, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=30, null=True)),
                ('RR_NO', models.IntegerField(blank=True, null=True)),
                ('Stan_No', models.IntegerField(blank=True, null=True)),
                ('Interchange', models.CharField(blank=True, max_length=30, null=True)),
                ('CardNo', models.CharField(blank=True, max_length=30, null=True)),
                ('CardType', models.CharField(blank=True, max_length=30, null=True)),
                ('TxnDate', models.CharField(max_length=30, null=True)),
                ('PaymentDate', models.CharField(blank=True, max_length=30, null=True)),
                ('PaymentRemarks1', models.CharField(blank=True, max_length=30, null=True)),
                ('K30_PRORATA_AMT', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('K30_Benefit_Received', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('TxnAmt', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('MdrMswipePer', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('MdrValue', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GST', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('TDS_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Deduction', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Conveyance_fees_Rate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Conveyance_fees_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Conveyance_fees_GST', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('NetAmt', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Rent', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Adjustment', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('FinalPayment', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('LoanDeductionRate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('LoanDeductionAmount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('AdditionalRecovery', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('FinalPaymentToMeAfterLoanDeduction', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('FinalPaymentToLoanProvider', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('REMARKS', models.CharField(blank=True, max_length=30, null=True)),
                ('Mswipe_Ref_No', models.IntegerField(blank=True, null=True)),
                ('NEFT_Ref_No', models.IntegerField(blank=True, null=True)),
                ('ARN', models.IntegerField(blank=True, null=True)),
                ('Lender_UTR_No', models.IntegerField(blank=True, null=True)),
                ('Lender_Payment_Date', models.CharField(blank=True, max_length=30, null=True)),
                ('Approval_No', models.IntegerField(blank=True, null=True)),
                ('Invoice_no', models.CharField(blank=True, max_length=30, null=True)),
                ('RowId', models.CharField(blank=True, max_length=30, null=True)),
                ('Cust_GroupCustCode', models.CharField(blank=True, max_length=30, null=True)),
                ('StoreCode', models.CharField(blank=True, max_length=30, null=True)),
                ('Cust_Device_Id', models.IntegerField(blank=True, null=True)),
                ('PaymentRemarks2', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_no', models.IntegerField(blank=True, null=True)),
                ('Merchant_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('DBA_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Merchant_Id', models.IntegerField(blank=True, null=True)),
                ('TID', models.IntegerField(blank=True, null=True)),
                ('Atom_Txn_ID', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('RRN', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('Auth_Code', models.IntegerField(null=True)),
                ('Currency', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Txn_Date', models.DateTimeField(null=True)),
                ('Txn_Type', models.IntegerField(blank=True, null=True)),
                ('Txn_Status', models.IntegerField(blank=True, null=True)),
                ('Recon_Status', models.CharField(blank=True, max_length=30, null=True)),
                ('Setteled_Date', models.DateField(blank=True, null=True)),
                ('Batch_number', models.IntegerField(blank=True, null=True)),
                ('Payment_Date', models.DateField(blank=True, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('MSF', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GST', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('GST_Slab', models.IntegerField(blank=True, null=True)),
                ('Cash_POS_Incent', models.IntegerField(blank=True, null=True)),
                ('net_Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('Local_Intl', models.CharField(blank=True, max_length=30, null=True)),
                ('mcc', models.IntegerField(blank=True, null=True)),
                ('City', models.CharField(blank=True, max_length=30, null=True)),
                ('Card_Number', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_Date', models.DateField(null=True)),
                ('Transaction_Details', models.CharField(max_length=50, null=True)),
                ('Cheque_ID', models.CharField(blank=True, max_length=30, null=True)),
                ('Value_Date', models.DateField(blank=True, null=True)),
                ('Withdrawl_Amt', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('Deposit_Amt', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('Balance_INR', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='type7',
            constraint=models.UniqueConstraint(fields=('Transaction_Date', 'Transaction_Details', 'Withdrawl_Amt', 'Deposit_Amt'), name='type7_unique'),
        ),
        migrations.AddConstraint(
            model_name='type6',
            constraint=models.UniqueConstraint(fields=('Atom_Txn_ID', 'RRN', 'Auth_Code', 'Txn_Date'), name='type6_unique'),
        ),
        migrations.AddConstraint(
            model_name='type5',
            constraint=models.UniqueConstraint(fields=('CustomerCode', 'TxnDate', 'FinalPayment'), name='type5_unique'),
        ),
    ]
