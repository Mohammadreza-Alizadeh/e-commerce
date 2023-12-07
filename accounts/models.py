from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

from django.utils.safestring import mark_safe

class User(AbstractBaseUser):
    
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default='No Bio')
    avatar = models.ImageField(upload_to='avatars', default='avatars/default-avatar.png')
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)


    def image_tag(self):
        return mark_safe(f'<img src="{self.avatar.url}" width="150" height="150" alt="avatar">')