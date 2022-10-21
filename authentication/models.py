from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class AcountManager(BaseUserManager):

    def create_user(self, email, user_name, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email adress')
        user = self.model(
            email = self.normalize_email(email), 
            user_name = user_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,user_name, password):
        user = self.create_user(email, password, user_name)
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique = True)
    user_name = models.CharField(max_length = 50)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = AcountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self) -> str:
        return self.user_name
    
    def get_short_name(self):
        return self.user_name[0]