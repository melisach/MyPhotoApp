from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from myPhotoApp.models.categorie import Categorie


class Photo(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=False, blank=False, default=None)
    description = models.TextField()
    date_creation = models.DateField(auto_now=True, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.description
