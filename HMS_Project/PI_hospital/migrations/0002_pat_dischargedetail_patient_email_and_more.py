# Generated by Django 4.2.2 on 2023-07-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat_dischargedetail',
            name='Patient_email',
            field=models.EmailField(default='abcd@gmail.com', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Admit_Date',
            field=models.DateField(auto_now=True),
        ),
    ]