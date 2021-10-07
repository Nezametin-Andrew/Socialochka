from django.db import models
from django.contrib.auth.models import AbstractUser
from soc_site import settings



class CustomUser(AbstractUser):
    ...


