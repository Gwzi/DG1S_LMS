# Generated by Django 5.0.3 on 2024-07-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_card_ip_precard_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precard',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
