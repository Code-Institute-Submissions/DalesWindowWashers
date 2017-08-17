# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, first_name, last_name, **extra_fields):
        now = timezone.now()
        if not User.objects.filter(email=self.cleaned_data['email']).exists():
            if not email:
                raise ValueError('The given username must be set')

            email = self.normalize_email(email)
            user = self.model(username=email, email=email, is_staff=is_staff,
                           is_active=True, is_superuser=is_superuser,
                           date_joined=now, first_name=first_name, last_name=last_name,
                           **extra_fields)

            user.set_password(password)
            user.save(using=self.__db)

            return user


class User(AbstractUser):
    objects = AccountUserManager()
