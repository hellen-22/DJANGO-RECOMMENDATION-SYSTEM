from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_number, email, password=None):
        if not registration_number:
            raise ValueError('Your Registration Number is required')

        if not email:
            raise ValueError('Email is required')

        user = self.model(
            registration_number=registration_number,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_number, email, password=None):
        user = self.create_user(
            registration_number=registration_number,
            email=self.normalize_email(email),
            password=password,
        )

       # user.set_password = password
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    registration_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=20, unique=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'registration_number'

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.registration_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True