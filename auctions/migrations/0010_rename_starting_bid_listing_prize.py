# Generated by Django 3.2.9 on 2021-12-04 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='prize',
        ),
    ]
