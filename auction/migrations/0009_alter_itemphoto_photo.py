# Generated by Django 4.1.7 on 2023-04-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_itemphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='item_images'),
        ),
    ]
