from django.views.generic import DetailView
from myPhotoApp.models.photo import Photo
from django.contrib.auth.mixins import LoginRequiredMixin


class PhotoView(LoginRequiredMixin, DetailView):
    template_name = 'photos/photo.html'
    model = Photo

