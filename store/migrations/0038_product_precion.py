# Generated by Django 3.0.8 on 2020-10-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_order_adrres'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Precion',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
