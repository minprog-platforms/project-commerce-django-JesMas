# Generated by Django 3.2.9 on 2021-12-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='listing',
            name='url',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
