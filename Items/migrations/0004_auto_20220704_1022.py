# Generated by Django 3.0.3 on 2022-07-04 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0003_ratingtable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemstable',
            name='rating',
        ),
        migrations.AddField(
            model_name='itemstable',
            name='avgRating',
            field=models.FloatField(db_column='avg_rating', default=0),
        ),
    ]
