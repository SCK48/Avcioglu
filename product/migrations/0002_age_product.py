# Generated by Django 3.1.4 on 2020-12-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Ad')),
                ('age', models.IntegerField(blank=True, verbose_name='Yaş')),
            ],
            options={
                'verbose_name': 'Yaş',
                'verbose_name_plural': 'Yaşlı',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ad')),
                ('keywords', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/', verbose_name='Resim')),
                ('status', models.CharField(choices=[('Açık', 'Açık'), ('Kapalı', 'Kapalı')], max_length=10, verbose_name='Durum')),
                ('price', models.IntegerField(verbose_name='Fiyat')),
                ('malzemeler', models.CharField(max_length=100, verbose_name='')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Ürün',
                'verbose_name_plural': 'Ürünler',
            },
        ),
    ]
