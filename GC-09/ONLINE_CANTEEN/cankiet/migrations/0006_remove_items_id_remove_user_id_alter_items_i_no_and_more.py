# Generated by Django 5.1.2 on 2024-11-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cankiet', '0005_canteen_alter_items_i_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='items',
            name='i_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
