# Generated by Django 3.2.9 on 2021-11-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_invoice_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.IntegerField(default=1),
        ),
    ]
