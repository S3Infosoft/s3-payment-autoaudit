# Generated by Django 3.0.4 on 2020-04-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_type9'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type9',
            name='batch',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='type9',
            name='device_serial',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='type9',
            name='rrn',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='type9',
            name='transaction_type',
            field=models.CharField(max_length=150),
        ),
    ]
