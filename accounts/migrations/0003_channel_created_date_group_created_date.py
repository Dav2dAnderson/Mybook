# Generated by Django 5.1.4 on 2024-12-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]