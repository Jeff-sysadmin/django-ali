# Generated by Django 2.0.5 on 2019-07-03 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0029_weekyhours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekyhours',
            old_name='hours_date',
            new_name='hours',
        ),
    ]