# Generated by Django 3.2.25 on 2024-09-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0021_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='veg_nonveg',
            field=models.CharField(choices=[('v', 'veg'), ('nv', 'non-veg')], default='Veg', max_length=7),
        ),
    ]
