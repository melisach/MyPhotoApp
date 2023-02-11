from django.contrib import admin
from myPhotoApp.models.photo import Photo
from myPhotoApp.models.categorie import Categorie

admin.site.register(Categorie)
admin.site.register(Photo)
