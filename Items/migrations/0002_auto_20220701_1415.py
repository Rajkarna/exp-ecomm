# Generated by Django 3.0.3 on 2022-07-01 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemstable',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='itemstable',
            name='updated_by',
        ),
    ]
