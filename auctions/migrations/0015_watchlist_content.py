# Generated by Django 3.2.9 on 2021-12-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='content',
            field=models.BooleanField(default=False),
        ),
    ]