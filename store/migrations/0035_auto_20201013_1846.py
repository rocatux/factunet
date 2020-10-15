# Generated by Django 3.0.8 on 2020-10-14 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_auto_20201013_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('cancelar', 'Cancelar'), ('aprobado', 'Aprobado'), ('procesando', 'Procesando'), ('completado', 'Compleatado'), ('aumentar', 'Aumentar')], max_length=10),
        ),
    ]
