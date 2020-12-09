# Generated by Django 3.1.4 on 2020-12-09 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201202_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('status', models.BooleanField(verbose_name='Durum')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.setting')),
            ],
        ),
    ]