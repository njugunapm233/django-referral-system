# Generated by Django 2.2.14 on 2020-08-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_referral_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='paystack_link',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]