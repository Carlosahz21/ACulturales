# Generated by Django 3.1 on 2020-09-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACulturales', '0004_auto_20200901_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parroquia',
            name='direccion_parroquia',
            field=models.CharField(max_length=60, verbose_name='direccion GAD'),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='nombre_parroquia',
            field=models.CharField(max_length=50, verbose_name='parroquia'),
        ),
        migrations.AlterField(
            model_name='parroquia',
            name='nombre_presidente',
            field=models.CharField(max_length=60, verbose_name='presidente'),
        ),
    ]
