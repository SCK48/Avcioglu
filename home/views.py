import json

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from home.forms import OrderForm, SearchForm
from home.models import Setting, ContactForm, ContactFormMessage, FAQ, SettingGallery
from product.models import Category, Product, Slider, Order, Images
from utils.mail import send_html_mail
from .mail_content import get_mail_content, get_mail_content2
from django.core.mail import send_mail

def index(request):
    category = Category.objects.filter(status='Açık').order_by('name')
    product = Product.objects.filter(status='Açık').order_by('?')[:6]
    setting = Setting.objects.get(pk=1)
    slider = Slider.objects.filter(status=True).order_by('-id')
    # content = Content.objects.filter(status='On')
    context = {
        'category': category,
        'setting': setting,
        'slider': slider,
        'product': product,
        'page': 'home',

    }
    return render(request, "index.html", context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkürler")
            return HttpResponseRedirect('/iletisim')
        else:
            messages.warning(request, 'HATA!<br>' + str(form.errors))
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.filter(status='Açık').order_by('name')
    form = ContactForm
    context = {
         'form': form,
         'setting': setting,
         'category': category,
        'page': 'iletisim',
     }
    return render(request, "contact.html", context)

def aboutus(request):
    category = Category.objects.filter(status='Açık').order_by('name')
    setting = Setting.objects.get(pk=1)
    gallery = SettingGallery.objects.filter(status=True)
    context = {
        'category': category,
        'setting': setting,
        'gallery': gallery,
        'page': 'about',
    }
    return render(request, "aboutus.html", context)

def faq(request):
    category = Category.objects.filter(status='Açık').order_by('name')
    faq = FAQ.objects.filter()
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'faq': faq,
        'page': 'faq',
    }
    return render(request, "faq.html", context)

def category(request):
    category = Category.objects.filter(status='Açık').order_by('name')
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'page': 'category',
    }
    return render(request, "category.html", context)

def category_detail(request, id, slug):
    category = Category.objects.filter(status='Açık').order_by('name')
    current_cat = Category.objects.get(pk=id)
    products = Product.objects.filter(status='Açık', category_id=id)
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'current_cat': current_cat,
        'products': products,
        'page': 'category',
    }
    return render(request, "products.html", context)

def product_detail(request,id,slug):
    url = request.META.get('HTTP_REFERER')
    category = Category.objects.filter(status='Açık').order_by('name')
    product = Product.objects.get(pk=id)
    related_products = Product.objects.filter(category_id=product.category_id, status='Açık')[:4]
    product_gallery = Images.objects.filter(product_id=id)
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.note = form.cleaned_data['note']
            data.quantity = form.cleaned_data['quantity']
            data.product = form.cleaned_data['product']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            # latestorder = Order.objects.latest('id')
            send_mail('Siparişiniz Alındı',
                      get_mail_content().format(name=data.name, product=data.product, quantity=data.quantity),
                      'Avcıoğlu Tarım <info@avcioglutarim.com>',
                      recipient_list=[data.email],
                      fail_silently=False)
            # send_html_mail('Siparişiniz Alındı',
            #           get_mail_content().format(name=data.name, product=data.product, quantity=data.quantity),
            #           recipient_list=[data.email], sender='Avcıoğlu Tarım <info@avcioglutarim.com>'
            #           )
            # send_html_mail(f'Yeni Sipariş #{latestorder.id}',
            #                get_mail_content2().format(name=data.name,
            #                                          product=data.product,
            #                                          quantity=data.quantity,
            #                                          note=data.note,
            #                                          id =latestorder.id,
            #                                          mail=data.email,
            #                                          phone=data.phone),
            #                recipient_list=[setting.email]
            #                )
            messages.success(request,
                             "Siparişiniz Alınmıştır, En Kısa Sürede Telefon ile Geri Dönüş Yapılacaktır.")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(url)
    context = {
        'category': category,
        'setting': setting,
        'product': product,
        'related_products': related_products,
        'product_gallery': product_gallery,
        'page': 'product',
    }
    return render(request, "product_detail.html", context)


def handler404(request, exception):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, '404.html', context)

def handler500(request):
    setting = Setting.objects.get(pk=1)
    context = {
        'setting': setting,
    }
    return render(request, '500.html', context)

def gallery(request):
    category = Category.objects.filter(status='Açık').order_by('name')
    images = Product.objects.filter(status='Açık').order_by('?')
    paginator = Paginator(images, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'images': images,
        'page_obj': page_obj,
        'page': 'gallery',
    }
    return render(request, 'gallery.html', context)

def product_search(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            return HttpResponse(products)
            #return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.name
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

