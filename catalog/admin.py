from django.contrib import admin
from catalog.models import Category, Product
from mptt.admin import MPTTModelAdmin
from django import forms
from ckeditor.widgets import CKEditorWidget


admin.site.register(Category, MPTTModelAdmin)


class ProductAdminForm(forms.ModelForm):
    characteristic = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm


admin.site.register(Product, ProductAdmin)



