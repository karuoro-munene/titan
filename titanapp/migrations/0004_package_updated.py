# Generated by Django 5.0.6 on 2024-06-21 20:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanapp', '0003_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]