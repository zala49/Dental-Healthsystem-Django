from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.hashers import make_password

# Custom UserManager
class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Email is require')
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('mobile', "1234567890")

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('super user must have is_stuff true'))

        return self.create_user(email, password, **extra_fields)


# User Details
class User(AbstractUser):
    username = None
    mobile = models.IntegerField(unique=True)
    email = models.EmailField("Email", unique=True)
    date_joined = models.DateField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def verify_password(self ,raw_password):
        return pbkdf2_sha256.verify_password(raw_password, self.password)

    def __str__(self):
        return self.email