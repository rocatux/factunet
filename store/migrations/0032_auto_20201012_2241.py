# Generated by Django 3.0.8 on 2020-10-13 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='season',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]
