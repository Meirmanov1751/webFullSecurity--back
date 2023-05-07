from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils.translation import gettext as _
from django.db import models


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    class ROLES:
        MANAGEMENT_COMPANY = 'management_company'
        EXECUTOR = 'executor'
        CUSTOMER = 'customer'
        USER = 'user'
        SUPER_ADMIN = 'super_admin'
        AUDITOR = 'auditor'

        ROLES_CHOICES = ((MANAGEMENT_COMPANY, "Басқарушы компания"), (USER, "Пайдаланушы"),
                         (SUPER_ADMIN, 'Супер әкімші'),
                         (EXECUTOR, 'Орындаушы'), (CUSTOMER, 'Тұтынушы'),
                         (AUDITOR, 'Аудитор')
                         )

    username = models.CharField(max_length=1000, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES.ROLES_CHOICES,
                            default=ROLES.USER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = UserManager()

    def __str__(self):
        return f'Email: {self.email}; Role: {self.role}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_super_admin(self):
        return self.role == User.ROLES.SUPER_ADMIN

    @property
    def is_user(self):
        return self.role == User.ROLES.USER

    @property
    def is_executor(self):
        return self.role == User.ROLES.EXECUTOR

    @property
    def is_customer(self):
        return self.role == User.ROLES.CUSTOMER

    @property
    def is_auditor(self):
        return self.role == User.ROLES.AUDITOR

    @property
    def is_management_company(self):
        return self.role == User.ROLES.MANAGEMENT_COMPANY

    class Meta:
        verbose_name = 'Пайдаланушы'
        verbose_name_plural = 'Пайдаланушылар'
