from django.db import models
from django.contrib.auth.models import AbstractUser
from soc_site import settings



class CustomUser(AbstractUser):
    ...
    avatar = models.ImageField("", upload_to="media/Y%/m%/d%/")
    phone = models.CharField("", max_length=12, blank=True)
    
    



