from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Age, Variants, Slider, Order, Images


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    def category_urun_count(self, obj):
        return obj.product_set.count()

    category_urun_count.short_description = "Ürün Sayısı"
    list_display = ['name', 'id', 'status', 'category_urun_count']
    prepopulated_fields = {'slug': ('name',)}

class ProductVariantsInline(admin.TabularInline):
    model = Variants
    extra = 1
    show_change_link = True

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'keywords', 'category', 'image_tag', 'variant', 'status']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductVariantsInline, ProductImageInline]
    list_filter = ['status', 'category',]

class VariantAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'age', 'price']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['product', 'description', 'category', 'status']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'product', 'status', 'create_at',]
    list_filter = ['status']
    readonly_fields = ('name', 'phone', 'email', 'create_at', 'quantity', 'note', 'update_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Age)
admin.site.register(Variants, VariantAdmin)
admin.site.register(Slider, SliderAdmin)