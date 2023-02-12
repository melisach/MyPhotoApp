"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another config
    1. Import the included() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from myPhotoApp.views.update_photo import UpdatePhotoView
from myPhotoApp.views.ajouter_categorie import AddCategorieView
from myPhotoApp.views.ajouter_photo import AddPhotoView
from myPhotoApp.views.ajouter_register import RegisterFormView
from myPhotoApp.views.delete_photo import DeletePhotoView
from myPhotoApp.views.index import IndexView
from myPhotoApp.views.photo import PhotoView
from myPhotoApp.views.gallerie import GallerieView
from django.conf import settings
from django.conf.urls.static import static
from myPhotoApp.views.user_gallerie import UserGallerieView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'index'),
    path('inscription', RegisterFormView.as_view(), name='register_form'),
    path('gallerie/', GallerieView.as_view(), name='gallerie'),
    path('photo/<str:pk>/', PhotoView.as_view(), name='photo'),
    path('ajouter_photo/', AddPhotoView.as_view(), name='ajouter_photo'),
    path('ajouter_categorie/', AddCategorieView.as_view(), name='ajouter_categorie'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', UserGallerieView.as_view(), name='user_gallerie'),
    path('<pk>/delete/', DeletePhotoView.as_view(), name='delete_photo'),
    path('<pk>/update/', UpdatePhotoView.as_view(), name='update_photo'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)