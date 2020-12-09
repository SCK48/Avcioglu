"""avcioglu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin

from home import views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),

    path('iletisim/', views.contact, name='iletisim'),
    path('hakkimizda/', views.aboutus, name='hakkimizda'),
    path('ürünler/', views.category, name='ürünler'),
    path('ürün/', views.product_detail, name='ürün_detay'),
    path('galeri/', views.gallery, name='galeri'),
    path('kategori/<int:id>/<slug:slug>/', views.category_detail, name='kategori_detay'),
    path('ürün/<int:id>/<slug:slug>/', views.product_detail, name='kategori_detay'),
    path('SSS/', views.faq, name='SSS'),
    path('404/', views.handler500, name='404'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)