# Generated by Django 3.1.1 on 2020-12-20 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_favourites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='favourites',
            new_name='favourited',
        ),
    ]
