# Generated by Django 2.0.5 on 2019-05-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0015_auto_20190527_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status_visa',
            field=models.IntegerField(choices=[(1, 'None'), (2, 'Citizenship'), (3, 'Green Card'), (4, 'HB1'), (5, 'Third Party'), (6, 'Other')], default=2),
        ),
    ]