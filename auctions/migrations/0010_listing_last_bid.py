# Generated by Django 3.1.1 on 2020-12-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201228_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='last_bid',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
