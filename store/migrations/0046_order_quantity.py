# Generated by Django 3.0.8 on 2020-10-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_auto_20201015_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
