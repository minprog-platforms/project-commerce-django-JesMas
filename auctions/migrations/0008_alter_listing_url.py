# Generated by Django 3.2.9 on 2021-12-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listing_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='url',
            field=models.TextField(default='https://depositphotos.com/247872612/stock-illustration-no-image-available-icon-vector.html'),
        ),
    ]
