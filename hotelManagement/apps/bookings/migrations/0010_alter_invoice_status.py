# Generated by Django 3.2.9 on 2021-11-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.IntegerField(),
        ),
    ]
