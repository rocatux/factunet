# Generated by Django 3.0.8 on 2020-10-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_auto_20201015_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cant',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
