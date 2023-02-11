from django.db import models


class Categorie(models.Model):
    categorie = models.CharField( max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.categorie
