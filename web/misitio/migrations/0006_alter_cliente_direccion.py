# Generated by Django 4.1.2 on 2022-10-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misitio', '0005_alter_cliente_fechalta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
