# Generated by Django 3.0.4 on 2020-03-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20200312_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=25)),
                ('transaction_value_date', models.DateField(null=True)),
                ('transaction_posted_date', models.DateField(null=True)),
                ('mode_of_payment', models.CharField(max_length=100)),
                ('credit', models.CharField(max_length=7)),
                ('transaction_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
    ]
