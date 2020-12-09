from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactForm, ContactFormMessage, FAQ, SettingGallery
from product.models import Category, Product, Slider


def index(request):
    category = Category.objects.filter(status='Açık').order_by('id')
    product = Product.objects.filter(status='Açık').order_by('id')[:6]
    test = Category.objects.get(pk=1)
    setting = Setting.objects.get(pk=1)
    slider = Slider.objects.filter(status=True).order_by('-id')
    # content = Content.objects.filter(status='On')
    context = {
        'category': category,
        'test': test,
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
    category = Category.objects.filter(status='Açık').order_by('id')
    form = ContactForm
    context = {
         'form': form,
         'setting': setting,
         'category': category,
        'page': 'iletisim',
     }
    return render(request, "contact.html", context)

def aboutus(request):
    category = Category.objects.filter(status='Açık').order_by('id')
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
    category = Category.objects.filter(status='Açık').order_by('id')
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
    category = Category.objects.filter(status='Açık').order_by('id')
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'page': 'category',
    }
    return render(request, "category.html", context)

def category_detail(request, id, slug):
    category = Category.objects.filter(status='Açık').order_by('id')
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
    category = Category.objects.filter(status='Açık').order_by('id')
    product = Product.objects.get(pk=id)
    related_products = Product.objects.filter(category_id=product.category_id, status='Açık')
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'product': product,
        'related_products': related_products,
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
    category = Category.objects.filter(status='Açık').order_by('id')
    images = Product.objects.filter(status='Açık')
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