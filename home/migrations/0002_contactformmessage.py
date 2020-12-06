# Generated by Django 3.1.4 on 2020-12-02 15:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='isim')),
                ('email', models.CharField(max_length=50, verbose_name='E-Mail')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon')),
                ('message', models.CharField(max_length=255, verbose_name='Mesaj')),
                ('status', models.CharField(choices=[('Yeni', 'Yeni'), ('Okundu', 'Okundu')], default='Yeni', max_length=10, verbose_name='Durum')),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme')),
            ],
            options={
                'verbose_name': 'Mesaj',
                'verbose_name_plural': 'Mesajlar',
            },
        ),
    ]