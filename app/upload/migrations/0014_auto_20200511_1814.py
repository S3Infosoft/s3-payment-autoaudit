# Generated by Django 3.0.4 on 2020-05-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0013_auto_20200429_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type1',
            field=models.ManyToManyField(to='upload.Type1'),
        ),
        migrations.AddField(
            model_name='customer',
            name='type9',
            field=models.ManyToManyField(to='upload.Type9'),
        ),
    ]
