# Generated by Django 2.0.5 on 2019-06-17 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20190609_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.ManyToManyField(blank=True, to='client.Contact'),
        ),
    ]
