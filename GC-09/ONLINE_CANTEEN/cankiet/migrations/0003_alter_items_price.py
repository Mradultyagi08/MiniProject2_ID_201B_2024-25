# Generated by Django 5.1.2 on 2024-11-25 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cankiet', '0002_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(),
        ),
    ]
