from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from projects.models import Project


class AdminManager(BaseUserManager):
    def create_admin(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        admin = self.model(username=username, **extra_fields)
        admin.set_password(password)
        admin.save()
        return admin

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        admin = self.create_admin(
            username,
            password=password
        )
        admin.is_superuser = True
        admin.is_staff = True
        admin.save(using=self._db)
        return admin

    def get_by_natural_key(self, username):
        return self.get(username=username)


class Admin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='admins', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = AdminManager()

    def __str__(self):
        return str(self.username)
