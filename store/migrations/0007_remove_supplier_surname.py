# Generated by Django 3.0.8 on 2020-10-10 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_supplier_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='surname',
        ),
    ]