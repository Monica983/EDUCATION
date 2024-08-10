from datetime import timezone
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

from module.models import Module

class AccountManager( BaseUserManager):
    def create_superuser(self, first_name, last_name, email, regstration_number, password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            regstration_number = regstration_number,
        )
        
        user.set_password(password)
        user.is_admin = True
        user.is_instructor = True
        user.is_student = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def create_user(self, first_name, last_name, email, registration_number, password=None):
        if not email:
            raise ValueError('user must enter an Email')
        if not registration_number:
            raise ValueError('user must enter a RegistrationNumber')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = registration_number,
        )
    
    
class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    registration_number = models.IntegerField(max_length=14, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    # modules = models.ManyToManyField(Module)


    

    REQUIRED_FIELDS = ['first_name', 'regstrationnumber', 'last_name']
    USERNAME_FIELD = 'email'
    objects = AccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email

    def set_password_for_user(self, user, password):
        user.set_password(password)
        user.save()

    class Meta:
        verbose_name = "account"
        verbose_name_plural = 'accounts'
    
    





