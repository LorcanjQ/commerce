# Generated by Django 3.1.1 on 2020-12-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201226_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='start_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=225),
        ),
    ]
