from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser
# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.SET_NULL)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('parent', 'slug', )
        verbose_name_plural = 'categories'

    @property
    def get_category_level(self):
        return self.get_level()

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []

        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'categories/{self.slug}/'


class Product(models.Model):
    category = TreeForeignKey('Category', null=True, blank=True, verbose_name='Категорія товару',
                              on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey('Brand', models.CASCADE, blank=True, null=True, verbose_name='бренд')
    slug = models.SlugField()
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва товару')
    image = models.ImageField(upload_to='product/', blank=True, verbose_name='Зображення товару')
    description = models.TextField(blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна зі знижкою')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    characteristic = RichTextField(blank=True, null=True, verbose_name='Характеристики')
    review_video = models.URLField(null=True, blank=True, verbose_name='Відео огляд')
    available = models.BooleanField(default=True, verbose_name='Доступний')

    class Meta:
        ordering = ['name']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    path = ArrayField(models.IntegerField())
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_feedback')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user_feedback')
    content = models.TextField('Відгук', max_length=1024)
    pub_date = models.DateTimeField('Дата створення відгуку', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def get_offset(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        level = len(self.path) - 1
        if level > 5:
            level = 5
        return 12 - level

    def __str__(self):
        return self.content[0:200]


class Brand(models.Model):
    name = models.CharField('Назва бренду', max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

