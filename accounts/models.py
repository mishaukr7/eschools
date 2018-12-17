from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Пошта', unique=True)
    first_name = models.CharField("Ім'я", max_length=30, blank=True)
    last_name = models.CharField('Прізвище', max_length=30, blank=True)
    date_joined = models.DateTimeField('Дата реєстрації', auto_now_add=True)
    is_active = models.BooleanField('Активний', default=False)
    is_staff = models.BooleanField('Адмін', default=False)

    portal_code = models.CharField('Код з порталу', max_length=255, null=True, blank=True)
    phone = models.DecimalField(
        'Номер телефону',
        max_digits=10,
        decimal_places=0,
        unique=True,
        null=True,
        blank=True,
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)],
        error_messages={
            'min_value': 'Номер телефону вказується без вісімки, повинен містити 10 цифр і не повинен починатися з нуля',
            'unique': 'Пользователь с таким номера телефона уже существует',
        },
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Користувачі')
        verbose_name_plural = _('Користувачі')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.get_full_name()
