# Generated by Django 2.0.5 on 2019-06-26 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0024_auto_20190626_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='client.Client'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='fee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='fee_management.Fee'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.Job'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='recruiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
