# Generated by Django 3.1.7 on 2021-03-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210306_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='profile_completed',
            field=models.BooleanField(default=False),
        ),
    ]
