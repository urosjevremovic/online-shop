# Generated by Django 2.0.7 on 2018-07-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_Order and OrderItem models added'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
