# Generated by Django 2.2.3 on 2019-08-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0044_contactemail_contactphone'),
        ('client', '0013_auto_20190809_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.ManyToManyField(blank=True, to='candidate.ContactEmail'),
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.ManyToManyField(blank=True, to='candidate.ContactPhone'),
        ),
    ]
