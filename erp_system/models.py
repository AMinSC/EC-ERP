from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create a new superuser profile """
        user = self.create_user(email,name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Authority(models.Model):
    authority_id = models.CharField(max_length=255, unique=True)
    authority_name = models.CharField(max_length=255)
    authority_menu = models.CharField(max_length=255)
    authority_level_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.authority_name


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    Authority_id = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='authority')
    name = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    addr2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    initialized = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self) -> str:
        """ Return string representation of our user """
        return self.email


class AuthorityMenu(models.Model):
    authority_menu_code = models.IntegerField(unique=True)
    authority_menu_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.authority_menu_name


class Dealer(models.Model):
    pass


class Client(models.Model):
    pass


class ASRegister(models.Model):
    pass


class History(models.Model):
    pass


class InstallationRequest(models.Model):
    pass


class Contractor(models.Model):
    pass


class Combo(models.Model):
    pass

