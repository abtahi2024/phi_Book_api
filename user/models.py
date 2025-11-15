from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import CustomUserMamager
from .managers import CustomUserMamager
from django.db import models
# Create your models here.
class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True,null=True)

    USERNAME_FIELD='email'#user email instead of username
    REQUIRED_FIELDS=[]

    objects=CustomUserMamager()
    def __str__(self):
        return self.email