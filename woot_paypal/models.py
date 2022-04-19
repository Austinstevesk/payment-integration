from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db import models
import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, account_name, password=None):
        if not email:
            raise ValueError('Email is required')
        if not full_name:
            raise ValueError('Full name is required')
        if not account_name:
            raise ValueError('Account Name is required')
        if not password:
            raise ValueError('Password is required')
        
        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            account_name = account_name,
            password = password
        )

        user.set_password(password)
        user.save(using=self._db)

        return user



    def create_superuser(self, email, full_name, account_name, password=None):
        user = self.create_user(
            email = email,
            full_name = full_name,
            account_name = account_name,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(_("email"), max_length=254, unique=True)
    full_name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=50, unique=True)
    date_joined = models.DateField(_("date_joined"), auto_now=False, auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['account_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True




