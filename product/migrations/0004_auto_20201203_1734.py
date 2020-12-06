# Generated by Django 3.1.4 on 2020-12-03 14:34

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201203_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0, verbose_name='Hakkında'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variants',
            name='age',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.age', verbose_name='Yaş'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product.product', verbose_name='Ürün'),
        ),
        migrations.AlterField(
            model_name='variants',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Başlık'),
        ),
    ]
