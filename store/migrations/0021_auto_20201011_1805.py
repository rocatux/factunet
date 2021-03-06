# Generated by Django 3.0.8 on 2020-10-12 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_buyer_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balances',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='credit',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='discount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
