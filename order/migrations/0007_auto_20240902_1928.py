# Generated by Django 3.2.25 on 2024-09-02 19:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20240902_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 19, 28, 51, 730032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 19, 28, 51, 730202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 19, 28, 51, 730032, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 19, 28, 51, 730202, tzinfo=utc)),
        ),
    ]
