# Generated by Django 3.0.8 on 2020-10-12 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_auto_20201011_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='address',
        ),
    ]