# Generated by Django 4.1.7 on 2023-03-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_item_current_bid_item_end_time_item_initial_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='current_bid',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='initial_bid',
            field=models.PositiveIntegerField(),
        ),
    ]
