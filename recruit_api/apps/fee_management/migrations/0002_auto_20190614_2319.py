# Generated by Django 2.0.5 on 2019-06-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fee_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='am_commission_percent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='AM Commission percent'),
        ),
        migrations.AddField(
            model_name='fee',
            name='client_fee_amount',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Client Fee Amount'),
        ),
        migrations.AddField(
            model_name='fee',
            name='client_fee_percentage',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Client Fee Percentage'),
        ),
        migrations.AddField(
            model_name='fee',
            name='rc_commission_percent',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='RC Commission percent'),
        ),
    ]