from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Age, Variants


class CategoryAdmin(admin.ModelAdmin):
    # def category_urun_count(self, obj):
    #     return obj.urun_set.count()
    #
    # category_urun_count.short_description = "Ürün Sayısı"  V 'category_urun_count'
    list_display = ['name', 'id', 'status', ]
    prepopulated_fields = {'slug': ('name',)}

class ProductVariantsInline(admin.TabularInline):
    model = Variants
    extra = 1
    show_change_link = True

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'keywords', 'category', 'image_tag', 'variant', 'status']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductVariantsInline]
    list_filter = ['status', 'category',]

class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'age', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Age)
admin.site.register(Variants, VariantAdmin)