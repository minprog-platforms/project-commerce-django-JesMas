# Generated by Django 3.2.9 on 2021-12-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_remove_watchlist_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]