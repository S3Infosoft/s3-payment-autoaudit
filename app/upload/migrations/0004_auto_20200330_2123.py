# Generated by Django 3.0.4 on 2020-03-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_type8'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type8',
            name='id',
        ),
        migrations.AlterField(
            model_name='type8',
            name='transaction_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]
