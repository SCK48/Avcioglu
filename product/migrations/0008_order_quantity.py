# Generated by Django 3.1.4 on 2020-12-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
