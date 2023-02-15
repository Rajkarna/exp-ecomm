from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):

    def create_user(self, username, email, phonenumber, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        if phonenumber is None:
            raise TypeError('Users should have a phonenumber')

        user = self.model(username=username, phonenumber=phonenumber, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    userFirstName = models.CharField(max_length=255, db_column='user_name')
    lastName = models.CharField(max_length=255, db_column='last_name', null=True)
    password = models.CharField(max_length=255, db_column='password', null=False)
    email = models.EmailField(max_length=255, db_index=True, unique=True)
    phoneNumber = models.CharField(max_length=20, db_column='phone_number', unique=True, db_index=True, null=True)
    address = models.TextField(db_column='address',null=True)
    dob = models.DateTimeField(db_column='dob',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phonenumber']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }