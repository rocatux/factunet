# Generated by Django 3.0.8 on 2020-10-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_buyer_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='discount',
            field=models.PositiveIntegerField(max_length=7, null=True),
        ),
    ]
