# Generated by Django 3.2.9 on 2021-12-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='highest_bid',
            new_name='bid',
        ),
        migrations.AlterField(
            model_name='listing',
            name='url',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
