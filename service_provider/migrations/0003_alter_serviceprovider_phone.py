# Generated by Django 4.2.1 on 2023-05-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider', '0002_service_remove_serviceprovider_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='phone',
            field=models.CharField(default='00-00-00-00-00', max_length=20),
        ),
    ]
