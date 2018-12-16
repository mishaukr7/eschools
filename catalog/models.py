from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser
from django.core.exceptions import ValidationError
# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.SET_NULL)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('parent', 'slug', )
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

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

    def save(self, *args, **kwargs):
        if self.parent.level >= 3:
            raise ValidationError(u'Достигнута максимальная вложенность!')

        # ancestors = list(self.get_ancestors(include_self=True).values_list('name', flat=True))
        # self.slug = slugify(ancestors)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    category = TreeForeignKey('Category', null=True, blank=True, verbose_name='Категорія товару',
                              on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Код товару')
    brand = models.ForeignKey('Brand', models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва товару')
    description = models.TextField(blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    price_with_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна зі знижкою')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    review_video = models.URLField(null=True, blank=True, verbose_name='Відео огляд')
    available = models.BooleanField(default=True, verbose_name='Доступний')
    partner = models.ForeignKey('Partner', blank=True, null=True, on_delete=models.SET_NULL)
    best = models.BooleanField(default=False, verbose_name='Найкращий товар')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(Product, self).save(force_insert=False, force_update=False, using=None,
                                  update_fields=None)

    class Meta:
        ordering = ['name']
        index_together = [['id', 'slug']]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

    def __str__(self):
        return self.name

    def get_discount_rate(self):
        return 100 - 100 * self.price_with_discount / self.price


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/', null=True, blank=True, verbose_name='Зображення товару')
    image_per_url = models.URLField(null=True, blank=True, verbose_name='Линк на изображение')


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва магазину')

    class Meta:
        ordering = ['name']
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнери'

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    path = ArrayField(models.IntegerField())
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_feedback')
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.PROTECT, related_name='user_feedback')
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField('Відгук', max_length=1024)
    pub_date = models.DateTimeField('Дата створення відгуку', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

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


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE,
                                related_name='characteristics')
    characteristic_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.characteristic_type} -- {self.name} -- {self.value}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики продукту'
        unique_together = ['product', 'characteristic_type', 'name', 'value']

