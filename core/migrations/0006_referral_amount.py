# Generated by Django 2.2.14 on 2020-08-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='amount',
            field=models.FloatField(default='1500'),
        ),
    ]