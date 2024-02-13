from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):
    phone_number = models.CharField(
        verbose_name="phone number",
        max_length=11,
        unique=True,
    )
    username = models.CharField(max_length=31)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['username']

    def posts(self):
        return list(self.sellPosts.all()) + list(self.rentPosts.all())

    def __str__(self):
        return f'{self.username} - {self.phone_number}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
