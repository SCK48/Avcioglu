from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    title = models.CharField(max_length=50, verbose_name='Ad')
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=100, verbose_name='Açıklama')
    company = models.CharField(max_length=30, verbose_name='Şirket')
    address = models.CharField(max_length=100, verbose_name='Adres')
    phone = models.CharField(max_length=30, verbose_name='Telefon')
    email = models.CharField(max_length=30, verbose_name='Email')
    icon = models.ImageField(blank=True, upload_to='images/')
    whatsapp = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=50)
    aboutus = RichTextUploadingField(verbose_name='Hakkımızda')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Ayarlar'
        verbose_name_plural='Ayarlar'


class ContactFormMessage(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('Okundu', 'Okundu'),
    )
    name = models.CharField(max_length=20, verbose_name='isim')
    email = models.CharField(max_length=50, verbose_name='E-Mail')
    phone = PhoneNumberField(verbose_name='Telefon')
    message = models.CharField(max_length=255, verbose_name='Mesaj')
    status = models.CharField(max_length=10, choices=STATUS, default='Yeni', verbose_name='Durum')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Mesaj'
        verbose_name_plural='Mesajlar'

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder':'Ad & Soyad'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'value': '+90'}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Mesaj'}),
        }

class FAQ(models.Model):
    header = models.CharField(max_length=150, verbose_name='Başlık')
    answer = RichTextUploadingField(verbose_name='Cevap')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name='SSS'
        verbose_name_plural='SSS'