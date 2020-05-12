# Generated by Django 3.0.4 on 2020-04-29 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_auto_20200410_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('id_from_mvr', models.CharField(max_length=40)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(null=True)),
                ('checkout_date', models.DateField(null=True)),
                ('expected_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('realised_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('notes', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CashEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('date', models.DateField(null=True)),
                ('details', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.Customer')),
            ],
        ),
    ]