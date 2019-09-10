# Generated by Django 2.2.3 on 2019-07-24 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0041_auto_20190718_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='client.Client'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.Job'),
        ),
    ]
