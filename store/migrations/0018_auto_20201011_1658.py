# Generated by Django 3.0.8 on 2020-10-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20201011_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balances',
            field=models.PositiveIntegerField(max_length=7, null=True),
        ),
    ]
