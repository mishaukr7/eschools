from django.db import models
from catalog.models import Product
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):

    NOVAPOSHTA = 'NP'
    COURIER = 'CR'
    DRIVEWAY = 'DW'

    DELIVERY_TYPE_CHOICES = (
        (NOVAPOSHTA, 'Нова пошта'),
        (COURIER, "Доставка кур'єром по Києву"),
        (DRIVEWAY, 'Самовивіз з магазину партнерів'),
    )
    ORDER_STATUS_CHOICES = ()

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, default=None,
                                 on_delete=models.SET_NULL)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    customer_email = models.EmailField(blank=False, null=False)
    customer_phone = models.DecimalField(
        'номер телефону',
        max_digits=10,
        decimal_places=0,
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)],
        error_messages={
            'min_value': 'Номер телефону вказується без вісімки, повинен містити 10 цифр і не повинен починатися з нуля',
            'unique': 'Пользователь с таким номера телефона уже существует',
        },
    )
    city = models.CharField('Місто', max_length=100)
    delivery_type = models.CharField(
        max_length=2,
        choices=DELIVERY_TYPE_CHOICES,
        default=DRIVEWAY
    )
    customer_first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    customer_last_name = models.CharField(verbose_name='Прізвище', max_length=50, blank=True, null=True)
    customer_patronymic = models.CharField(verbose_name="По-батькові", max_length=50, blank=True, null=True)

    status = models.CharField(
        'Статус замовлення',
        max_length=32,
        choices=(
            ('processed', 'в обробці'),
            ('accepted', 'прийнято'),
            ('shipped', 'відправлено'),
            ('waiting', 'очікує в магазині'),
            ('canceled', 'скасовано'),
            ('paid', 'оплачено'),
        ),
        default='processed',
    )
    created = models.DateTimeField(verbose_name='Створений', auto_now_add=True)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення: {self.id}'

    @property
    def total_cost(self):
        return sum(item.fullt_item_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)

    def __str__(self):
        f'{self.id}: {self.product}'

    @property
    def full_item_cost(self):
        return self.price * self.quantity

