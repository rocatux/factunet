# Generated by Django 3.0.8 on 2020-10-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_supplier_tipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='tipe',
            field=models.CharField(choices=[('Principal', 'Principal'), ('Alterna', 'Alterna')], default='Principal', max_length=10),
        ),
    ]