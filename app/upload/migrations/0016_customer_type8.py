# Generated by Django 3.0.4 on 2020-05-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0015_auto_20200511_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type8',
            field=models.ManyToManyField(related_name='linked_customer', to='upload.Type8'),
        ),
    ]