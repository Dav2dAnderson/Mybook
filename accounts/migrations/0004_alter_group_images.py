# Generated by Django 5.1.4 on 2024-12-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_channel_created_date_group_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='group_images/'),
        ),
    ]
