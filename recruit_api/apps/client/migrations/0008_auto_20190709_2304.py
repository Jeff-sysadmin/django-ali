# Generated by Django 2.0.5 on 2019-07-09 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20190617_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name'], 'verbose_name_plural': 'Clients'},
        ),
    ]
