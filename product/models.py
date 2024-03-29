from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from django.views.generic import ListView


class Category(models.Model):
    STATUS = (
        ('Açık', 'Açık'),
        ('Kapalı', 'Kapalı'),
    )
    name = models.CharField(max_length=30)
    keywords = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('id',)
        verbose_name='Kategori'
        verbose_name_plural='Kategoriler'

    def image_tag(self):
        return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('kategori_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    STATUS = (
        ('Açık', 'Açık'),
        ('Kapalı', 'Kapalı'),
    )
    VARIANTS = (
        ('None', 'Yok'),
        ('Age', 'Yaş'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori')
    name = models.CharField(max_length=50, verbose_name='Ad')
    keywords = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', verbose_name='Resim')
    status = models.CharField(max_length=10, choices=STATUS, verbose_name='Durum')
    price = models.IntegerField(verbose_name='Fiyat')
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    date = models.CharField(max_length=200, verbose_name='Hasat Zamanı')
    about = RichTextUploadingField(verbose_name='Hakkında')
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="100"/>'.format(self.image.url))
    image_tag.short_description = 'Resim'

    def get_absolute_url(self):
        return reverse('design_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name='Ürün'
        verbose_name_plural='Ürünler'

class Images(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        title = models.CharField(max_length=50, blank=True)
        image = models.ImageField(blank=True, upload_to='images/')

        def __str__(self):
            return self.title

        class Meta:
            verbose_name = 'Fotoğraf'
            verbose_name_plural = 'Fotoğraflar'

class Age(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ad')
    age = models.IntegerField(blank=True, verbose_name='Yaş')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Yaş'
        verbose_name_plural='Yaşlı'

class Variants(models.Model):
    title = models.CharField(max_length=30, verbose_name='Başlık')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants', verbose_name='Ürün')
    age = models.ForeignKey(Age, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Yaş')
    price = models.FloatField(default=0, verbose_name='Fiyat')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Çeşitler'
        verbose_name_plural='Çeşitler'

class Slider(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün')
    keywords = models.CharField(max_length=30)
    description = models.TextField(max_length=300, verbose_name='Açıklama')
    status = models.BooleanField(verbose_name='Durum')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    @property
    def category(self):
        return (self.product.category)

    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Sliderlar'

class ProductList(ListView):
    paginate_by = 2
    model = Product

class Order(models.Model):
    DURUM = (
        ('Yeni', 'Yeni'),
        ('Hazırlanıyor', 'Hazırlanıyor'),
        ('Tamamlandı', 'Tamamlandı'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ürün')
    name = models.CharField(max_length=50, verbose_name='Ad&Soyad')
    phone = PhoneNumberField(verbose_name='Telefon')
    email = models.CharField(max_length=30, verbose_name='E-Posta')
    quantity = models.IntegerField(verbose_name='Adet')
    status = models.CharField(max_length=30, choices=DURUM, default='Yeni')
    note = models.CharField(blank=True, max_length=200, verbose_name='Açıklama')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Son Güncelleme')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Sipariş'
        verbose_name_plural='Siparişler'