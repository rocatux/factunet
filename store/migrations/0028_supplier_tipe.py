# Generated by Django 3.0.8 on 2020-10-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_supplier_phonesupplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='tipe',
            field=models.CharField(choices=[('Principal', 'Principal'), ('Alterna', 'Alterna')], default='M', max_length=10),
        ),
    ]
