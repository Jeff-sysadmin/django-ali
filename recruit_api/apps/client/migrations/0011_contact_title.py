# Generated by Django 2.2.3 on 2019-08-08 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_auto_20190807_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
