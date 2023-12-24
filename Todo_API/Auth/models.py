from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, name, dob, password=None, password2=None):
        if not email:
            raise ValueError("User must have a email address")

        if not name:
            raise ValueError("User must have  username")

        if not dob:
            raise ValueError("User must have date of birth")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            dob=dob
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dob, password=None):
        user = self.create_user(
            email=email,
            name=name,
            dob=dob,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=255)
    dob = models.DateField(blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'dob']

    objects = UserManager()

    def __str__(self):
        return f'Username: {self.name}, Email: {self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
