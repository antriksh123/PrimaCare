# Generated by Django 3.1.7 on 2021-03-07 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20210307_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='security_key',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
