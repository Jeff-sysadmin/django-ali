# Generated by Django 2.0.5 on 2019-06-26 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0026_thirdparty'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='third_party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='candidate.ThirdParty'),
        ),
    ]
