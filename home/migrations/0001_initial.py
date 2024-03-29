# Generated by Django 3.1.4 on 2020-12-01 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Ad')),
                ('keywords', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, verbose_name='Açıklama')),
                ('company', models.CharField(max_length=30, verbose_name='Şirket')),
                ('address', models.CharField(max_length=100, verbose_name='Adres')),
                ('phone', models.CharField(max_length=30, verbose_name='Telefon')),
                ('email', models.CharField(max_length=30, verbose_name='Email')),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('whatsapp', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('aboutus', models.CharField(max_length=50, verbose_name='Hakkımızda')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ayarlar',
                'verbose_name_plural': 'Ayarlar',
            },
        ),
    ]
