# Generated by Django 4.1.7 on 2023-03-29 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_alter_item_end_time_alter_item_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='item_images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.item')),
            ],
        ),
    ]
